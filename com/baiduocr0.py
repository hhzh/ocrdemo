from aip import AipOcr
import numpy as np
import os
import datetime

# my
# APP_ID = '9999224'
# API_KEY = 'eqDDM65ekpMTxGGXlM658Tvd'
# SECRET_KEY = 'BzUyA3S0IoqAmTBd0jGtZ0ghiIzB7dLi'

# qiaojian
# APP_ID = '9985116'
# API_KEY = 'wsOs6Ye6iEKqkH1czgBFWhWS'
# SECRET_KEY = 'H56jOxlyZmueLUHnsx7uZnGqXmhVHoZG'

# vip
APP_ID = '10073324'
API_KEY = 'zapROApDpKIY2xGF4LXwUTj4'
SECRET_KEY = 'Zx3S7lMIqaU3nl4b7X59A1FXGCQYdS8G'

paths = []

sss = datetime.datetime.now()


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


# 初始化ApiOcr对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 调用通用文字识别接口
traverse('/demo/im')
for imgpath in paths:
    start = datetime.datetime.now()

    path, name = os.path.split(imgpath)
    print('开始处理：' + imgpath)
    # with open(os.path.join(path, 'nohup.log'), 'a') as fp:
    #     fp.write('开始处理:' + imgpath)
    #     fp.write('\n')

    try:
        result = aipOcr.basicGeneral(get_file_content(imgpath))
        if result.get('words_result_num', 0) > 0:
            for obj in result['words_result']:
                with open(os.path.join(path, 'result.txt'), 'a') as fp:
                    fp.write(obj['words'])
                    fp.write('\n')
        else:
            with open('errorOcr.log', 'a') as fp:
                fp.write(imgpath + '---' + str(result))
                fp.write('\n')
            print('error:' + imgpath + '---' + str(result))
    except Exception as e:
        with open('errorOcr.log', 'a') as fp:
            fp.write(imgpath + '---' + str(e))
            fp.write('\n')
        print('error:' + imgpath + '---cause:' + str(e))

    finally:
        end = datetime.datetime.now()
        with open('ocr.txt', 'a') as fp:
            filesize = os.path.getsize(imgpath) / 1024 / 1024
            xxx = '{:.4f}'.format(filesize)
            fp.write(str(imgpath))
            fp.write('\t')
            fp.write(xxx)
            fp.write('\t')
            fp.write(str(end - start))
            fp.write('\n')

with open('ocr.txt', 'a') as fp:
    eee = datetime.datetime.now()
    fp.write('------')
    fp.write(str(eee - sss))
    fp.write('\n')
    fp.write(str(len(paths)))
    fp.write('\n')
