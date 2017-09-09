from aip import AipOcr
import numpy as np
import os
import threading

# my
# APP_ID = '9999224'
# API_KEY = 'eqDDM65ekpMTxGGXlM658Tvd'
# SECRET_KEY = 'BzUyA3S0IoqAmTBd0jGtZ0ghiIzB7dLi'

# # qiaojian
APP_ID = '9985116'
API_KEY = 'wsOs6Ye6iEKqkH1czgBFWhWS'
SECRET_KEY = 'H56jOxlyZmueLUHnsx7uZnGqXmhVHoZG'

# vip
# APP_ID = '10073324'
# API_KEY = 'zapROApDpKIY2xGF4LXwUTj4'
# SECRET_KEY = 'Zx3S7lMIqaU3nl4b7X59A1FXGCQYdS8G'

paths = []


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


def begin_ocr(imgpaths):
    for imgpath in imgpaths:
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
                with open(os.path.join(path, 'errorOcr.log'), 'a') as fp:
                    fp.write('error:' + imgpath + ' +++cause:' + str(result))
                    fp.write('\n')
                print('error:' + imgpath + '---cause:' + str(result))
        except Exception as e:
            with open(os.path.join(path, 'errorOcr.log'), 'a') as fp:
                fp.write('error:' + imgpath + ' ---cause:' + str(e))
                fp.write('\n')
            print('error:' + imgpath + '---cause:' + str(e))


def create_thread(imgpaths):
    x = 0
    splitpaths = []
    splitsize = int(len(imgpaths) / 5)
    while x < len(imgpaths):
        splitpaths.append(imgpaths[x:x + splitsize])
        x = x + splitsize
    ths = []
    for splitpath in splitpaths:
        th = threading.Thread(target=begin_ocr, args=(splitpath,))
        ths.append(th)
    for i in ths:
        i.start()
    for i in ths:
        i.join()


if __name__ == "__main__":
    # 初始化ApiOcr对象
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    traverse('d:/demo')
    create_thread(paths)
