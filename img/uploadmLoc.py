import os

import cv2
import numpy as np
import requests
import pymysql
import logging
from aip import AipOcr
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

paths = []

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='nohup.log',
                    filemode='w')


@app.route('/hello', methods=['GET'])
def hello():
    print('hello')
    result = ''
    with open(os.path.join(os.path.abspath('./img/95083e7bca6b09fb4c02e7cd666ab506'), 'result.txt'), 'r',
              encoding='utf-8') as fp:
        for line in fp.readlines():
            result = result + line
    print('result:' + result)
    data = {'aa': 'aa', 'bb': result}
    return jsonify(data)


@app.route('/uploadMD5', methods=['POST'])
def upload_MD5():
    if request.method == 'POST':
        imgMD5 = request.form['md5']
        response = requests.get('http://www.carecnn.com/' + imgMD5)
        if response.status_code == 200:
            if not os.path.exists(os.path.join(os.path.abspath('./img'), imgMD5)):
                os.makedirs(os.path.join(os.path.abspath('./img'), imgMD5))
                with open('./img/info.log', 'a', encoding='utf-8') as fp:
                    fp.write('创建目录:' + os.path.join(os.path.abspath('./img'), imgMD5))
                    logging.info('创建目录：%s' % os.path.join(os.path.abspath('./img'), imgMD5))
                    fp.write('\n')
            with open('./img/' + imgMD5 + '/upload.jpg', 'wb') as fp:
                fp.write(response.content)
            return end_process(imgMD5)


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        imgData = request.files['file']
        imgData.save('./img/img.jpg')
        print('保存图片 %s 成功！' % imgData.filename)
        logging.info('保存图片 %s 成功！' % imgData.filename)
        with open('./img/info.log', 'a', encoding='utf-8') as fp:
            fp.write('保存图片:' + imgData.filename + ' 在 ' + os.path.join(os.path.abspath('./img'), 'img.jpg'))
            fp.write('\n')

        files = {'file': open(os.path.join(os.path.abspath('./img'), 'img.jpg'), 'rb')}

        response = requests.post('http://www.carecnn.com/upload', files=files)
        if response.status_code == 200:
            lines = response.text.splitlines()
            for line in lines:
                if line.startswith('<h1>MD5'):
                    imgMD5 = line[line.index('<h1>MD5:') + 8:line.index('</h1>')].strip()
                    if not os.path.exists(os.path.join(os.path.abspath('./img'), imgMD5)):
                        os.makedirs(os.path.join(os.path.abspath('./img'), imgMD5))
                        with open('./img/info.log', 'a', encoding='utf-8') as fp:
                            fp.write('创建目录:' + os.path.join(os.path.abspath('./img'), imgMD5))
                            fp.write('\n')
                    with open('./img/' + imgMD5 + '/upload.jpg', 'wb') as fp:
                        fp.write(open('./img/img.jpg', 'rb').read())
                    # os.remove('./img/img.jpg')
                    print('上传图片 %s 成功！' % imgMD5.strip())

                    with open('./img/info.log', 'a', encoding='utf-8') as fp:
                        fp.write('上传图片 %s 成功！' % imgMD5)
                        fp.write('\n')

                    return end_process(imgMD5)

        return 'ocr error.'


def cv_img(imgMD5):
    afile = os.path.join(os.path.abspath('./img/' + imgMD5), 'upload.jpg')
    # afile = './img/' + imgMD5 + '/upload.jpg'
    filepath, filename = os.path.split(afile)

    img = cv2.imread(os.path.join(filepath, filename))

    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 300, apertureSize=3)

        # blur and threshold the image
        blurred = cv2.blur(edges, (11, 11))
        (_, thresh) = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (300, 300))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # perform a series of erosions and dilations
        closed = cv2.erode(closed, None, iterations=4)
        closed = cv2.dilate(closed, None, iterations=4)

        image, contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        c = sorted(contours, key=cv2.contourArea, reverse=True)

        mm = 1
        for cc in c:
            # compute the rotated bounding box of the largest contour
            rect = cv2.minAreaRect(cc)
            box = np.int0(cv2.boxPoints(rect))

            Xs = [i[0] for i in box]
            Ys = [i[1] for i in box]
            x1 = min(Xs) - 15
            x2 = max(Xs) + 15
            y1 = min(Ys) - 15
            y2 = max(Ys) + 15
            height = y2 - y1
            width = x2 - x1
            cropImg = img[y1:y1 + height, x1:x1 + width]

            cv2.imwrite(filepath + '/' + str(mm) + 'img.jpg', cropImg)

            cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
            mm = mm + 1
        cv2.imwrite(os.path.join(filepath, 'zresult.jpg'), img)
    except:
        with open(os.path.join(filepath, 'errorImg.log'), 'a') as fp:
            fp.write('error:' + afile)
            fp.write('\n')
        print("error:" + afile)


# 读取图片
def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()


def traverse(filepath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            traverse(fi_d)
        elif fi_d.endswith('img.jpg'):
            paths.append(os.path.join(filepath, fi_d))


def begin_ocr(imgMD5):
    # vip
    APP_ID = '10073324'
    API_KEY = 'zapROApDpKIY2xGF4LXwUTj4'
    SECRET_KEY = 'Zx3S7lMIqaU3nl4b7X59A1FXGCQYdS8G'

    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    traverse(os.path.join(os.path.abspath('./img'), imgMD5))

    for imgpath in paths:
        path, name = os.path.split(imgpath)
        print('开始处理：' + imgpath)
        logging.info('开始处理：%s' % imgpath)
        with open(os.path.join(path, 'info.log'), 'a', encoding='utf-8') as fp:
            fp.write('开始处理:' + imgpath)
            fp.write('\n')

        try:
            result = aipOcr.basicGeneral(get_file_content(imgpath))
            if result.get('words_result_num', 0) > 0:
                for obj in result['words_result']:
                    with open(os.path.join(path, 'result.txt'), 'a', encoding='utf-8') as fp:
                        fp.write(obj['words'])
                        fp.write('\n')
            else:
                with open(os.path.join(path, 'errorOcr.log'), 'a', encoding='utf-8') as fp:
                    fp.write('error:' + imgpath + ' ---cause:' + str(result))
                    fp.write('\n')
                print('error:' + imgpath + '---cause:' + str(result))
        except Exception as e:
            with open(os.path.join(path, 'errorOcr.log'), 'a', encoding='utf-8') as fp:
                fp.write('error:' + imgpath + ' ---cause:' + str(e))
                fp.write('\n')
            print('error:' + imgpath + '---cause:' + str(e))


def end_process(imgMD5):
    cv_img(imgMD5)
    begin_ocr(imgMD5)

    print('md5:' + imgMD5)
    if not os.path.exists(os.path.join(os.path.abspath('./img/' + imgMD5), 'result.txt')):
        return 'ocr error.'
    else:
        result = ''
        with open(os.path.join(os.path.abspath('./img/' + imgMD5), 'result.txt'), 'r',
                  encoding='utf-8', errors='ignore') as fp:
            for line in fp.readlines():
                result = result + line
        print('result:' + result)
        conn = pymysql.connect(host='114.112.104.149', port=3306, user='root', passwd='SCMD_2017_scmd', db='scmd',
                               charset='utf8')
        cursor = conn.cursor()
        # result = '桥上吊刀'
        sql = 'insert into sc_ocr (imgMD5,result) values (%s,%s)'
        exec_result = cursor.execute(sql, (imgMD5, result))
        conn.commit()
        conn.close()
        # return 'OK'
        # return jsonify({'imgMD5': imgMD5})
        return result
        # return jsonify({'imgMD5': imgMD5, 'result': result})


if __name__ == '__main__':
    app.run()
    # app.run(host='114.112.104.150', port=5000)
