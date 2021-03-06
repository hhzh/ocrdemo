import os

import cv2
import numpy as np
import requests
import pymysql
import logging
import threading
# import ocrrequest_pb2
import socket
import shutil
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
    data = {'result': 'hello'}
    return jsonify(data)


@app.route('/uploadMD5', methods=['POST'])
def upload_MD5():
    if request.method == 'POST':
        imgMD5 = request.form['imgMD5']
        userId = request.form.get('userId')
        # userId = request.form['userId']
        caseType = request.form.get('caseType')
        # caseType = request.form['caseType']
        logging.info('接受请求/uploadMD5, imgMD5:%s, userId:%s, caseType=%s', imgMD5, userId, caseType)
        response = requests.get('http://www.carecnn.com/' + imgMD5)
        if response.status_code == 200:
            if not os.path.exists(os.path.join(os.path.abspath('./img'), imgMD5)):
                os.makedirs(os.path.join(os.path.abspath('./img'), imgMD5))
                logging.info('创建目录：%s', os.path.join(os.path.abspath('./img'), imgMD5))
            with open('./img/' + imgMD5 + '/upload.jpg', 'wb') as fp:
                fp.write(response.content)
            return cv_img(imgMD5, userId, caseType)


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        imgData = request.files['file']
        userId = request.args.get('userId')
        # userId = request.args['userId']
        caseType = request.args.get('caseType')
        # caseType = request.args['caseType']
        logging.info('接受请求/upload, userId=%s, caseType=%s', userId, caseType)
        imgData.save('./img/img.jpg')
        logging.info('保存图片：%s 在 %s', imgData.filename, os.path.join(os.path.abspath('./img'), 'img.jpg'))

        files = {'file': open(os.path.join(os.path.abspath('./img'), 'img.jpg'), 'rb')}
        response = requests.post('http://www.carecnn.com/upload', files=files)
        if response.status_code == 200:
            lines = response.text.splitlines()
            for line in lines:
                if line.startswith('<h1>MD5'):
                    imgMD5 = line[line.index('<h1>MD5:') + 8:line.index('</h1>')].strip()
                    logging.info('上传图片 %s 成功！', imgMD5)
                    return cv_img(imgMD5, userId, caseType)

        return 'ocr error.'


def cv_img(imgMD5, userId, caseType):
    afile = os.path.join(os.path.abspath('./img'), 'img.jpg')
    filepath, filename = os.path.split(afile)

    img = cv2.imread(os.path.join(filepath, filename))

    images = []

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
        # c = sorted(contours, key=cv2.contourArea, reverse=True)
        c = sorted(contours, key=lambda con: min(con[:, 0, 1]))

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

            if x1 < 0:
                x1 = 0
            if y1 < 0:
                y1 = 0

            cropImg = img[y1:y1 + height, x1:x1 + width]

            if isinstance(caseType, str) and caseType == 'reportCard':
                pts1 = np.float32(
                    [[box[2][0] - 20, box[2][1] - 20], [box[3][0] + 20, box[3][1] - 20],
                     [box[1][0] - 20, box[1][1] + 20],
                     [box[0][0] + 20, box[0][1] + 20]])
                pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
                M = cv2.getPerspectiveTransform(pts1, pts2)
                cropImg = cv2.warpPerspective(img, M, (width, height))

            # cv2.imwrite(filepath + '/' + str(mm) + 'img.jpg', cropImg)
            images.append(cropImg)

            # cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
            # cv2.imwrite(os.path.join(filepath, 'zresult.jpg'), img)
    except:
        logging.error('图片处理出错：%s', imgMD5)
    begin_ocr(imgMD5, images, userId, caseType)


def begin_ocr(imgMD5, images, userId, caseType):
    # vip
    APP_ID = '10073324'
    API_KEY = 'zapROApDpKIY2xGF4LXwUTj4'
    SECRET_KEY = 'Zx3S7lMIqaU3nl4b7X59A1FXGCQYdS8G'

    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    result_txt = ''

    for i, sub_img in enumerate(images):
        try:
            result = aipOcr.basicGeneral(sub_img)
            if result.get('words_result_num', 0) > 0:
                for obj in result['words_result']:
                    result_txt += obj['words']
                    result_txt += '\n'
            else:
                logging.warning('图片 %s 未识别：%s', imgMD5 + '/' + str(i), str(result))
        except Exception as e:
            logging.error('识别图片 %s 出错：%s', imgMD5, str(e))
    end_process(imgMD5, userId, caseType, result_txt)


def end_process(imgMD5, userId, caseType, result_txt):
    if result_txt == '':
        return 'ocr error.'
    else:
        conn = pymysql.connect(host='114.112.104.149', port=3306, user='root', passwd='SCMD_2017_scmd', db='scmd',
                               charset='utf8')
        cursor = conn.cursor()
        logging.info('插入数据库：imgMd5=%s, userId=%s, caseType=%s', imgMD5, userId, caseType)
        try:
            if userId is not None and userId != '' and userId != ' ':
                sql = 'insert into sc_ocr (userId,imgMD5,result) values (%s,%s,%s)'
                exec_result = cursor.execute(sql, (userId, imgMD5, result_txt))
            else:
                sql = 'insert into sc_ocr (imgMD5,result) values (%s,%s)'
                exec_result = cursor.execute(sql, (imgMD5, result_txt))
        except Exception as e:
            logging.error('插入数据库出错：imgMd5=%s, userId=%s, caseType=%s, %s', imgMD5, userId, caseType, e)
        conn.commit()
        conn.close()
        # return 'OK'
        # return jsonify({'result': result})
        # return jsonify({'imgMD5': imgMD5})
        return result_txt
        # return jsonify({'imgMD5': imgMD5, 'result': result})



if __name__ == '__main__':
    # app.run()
    app.run(host='114.112.104.150', port=5000)
