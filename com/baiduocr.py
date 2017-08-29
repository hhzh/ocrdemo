from aip import AipOcr
import numpy as np
import os

# my
# APP_ID = '9999224'
# API_KEY = 'eqDDM65ekpMTxGGXlM658Tvd'
# SECRET_KEY = 'BzUyA3S0IoqAmTBd0jGtZ0ghiIzB7dLi'

# qiaojian
APP_ID = '9985116'
API_KEY = 'wsOs6Ye6iEKqkH1czgBFWhWS'
SECRET_KEY = 'H56jOxlyZmueLUHnsx7uZnGqXmhVHoZG'

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


# 初始化ApiOcr对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 调用通用文字识别接口
traverse('d:/6yue3haoyufangtang')
for imgpath in paths:
    path, name = os.path.split(imgpath)
    print('开始处理：' + imgpath)
    with open(os.path.join(path, 'nohup.log'), 'a') as fp:
        fp.write('开始处理:' + imgpath)
        fp.write('\n')

    try:
        result = aipOcr.basicGeneral(get_file_content(imgpath))
        if result.get('words_result_num', 0) > 0:
            for obj in result['words_result']:
                with open(os.path.join(path, 'result.txt'), 'a') as fp:
                    fp.write(obj['words'])
                    fp.write('\n')
        else:
            with open(os.path.join(path, 'errorOcr.log'), 'a') as fp:
                fp.write('error:' + imgpath + ' ---cause:' + str(result))
                fp.write('\n')
            print('error:' + imgpath + '---cause:' + str(result))
    except Exception as e:
        with open(os.path.join(path, 'errorOcr.log'), 'a') as fp:
            fp.write('error:' + imgpath + ' ---cause:' + str(e))
            fp.write('\n')
        print('error:' + imgpath + '---cause:' + str(e))

# f = open('e:/demo/result.txt', 'a')
# for i in np.arange(1, 4):
#     result = aipOcr.basicGeneral(
#         get_file_content('D:\\6yue3haoyufangtang\\10_aijinhua_hengwenjirouliu\\1\\' + str(i) + 'img.jpg'))
#     print(result)
#     if result.get('words_result_num', 0) > 0:
#         print('hello')
#     else:
#         print('zzz')
# # if result['words_result_num'] > 0:
# #     for obj in result['words_result']:
# #         print(obj['words'])
# #         f.write(obj['words'])
# #         f.write('\n')
# f.close()

# 如果图片是url 调用示例如下
# result = aipOcr.basicGeneral('http://img0.ph.126.net/JgZPujjerZ1A7U_6gfs8Ag==/2515260391903843500.jpg')
# result = aipOcr.basicGeneral('https://img1.doubanio.com/lpic/s9155608.jpg')
#
# result = aipOcr.basicGeneral(get_file_content('e:/5.jpg'))
# # result = aipOcr.basicGeneral(get_file_content('e:/test/cropImg' + str(1) + '.jpg'))
# print(type(result))
# print(result)
# # print(result['words_result'])
