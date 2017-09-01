from aip import AipOcr
import numpy as np
import base64
import os
from time import ctime, sleep

# APP_ID = '9999224'
# API_KEY = 'eqDDM65ekpMTxGGXlM658Tvd'
# SECRET_KEY = 'BzUyA3S0IoqAmTBd0jGtZ0ghiIzB7dLi'

# vip
APP_ID = '10073324'
API_KEY = 'zapROApDpKIY2xGF4LXwUTj4'
SECRET_KEY = 'Zx3S7lMIqaU3nl4b7X59A1FXGCQYdS8G'


# 读取图片
def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()


# 初始化ApiOcr对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# # 调用通用文字识别接口
# f = open('e:/demo/result.txt', 'a')
# for i in np.arange(1, 10):
#     result = aipOcr.basicGeneral(get_file_content('e:/66/cropImg' + str(i) + '.jpg'))
#     if result['words_result_num'] > 0:
#         for obj in result['words_result']:
#             print(obj['words'])
#             f.write(obj['words'])
#             f.write('\n')
# f.close()

# 如果图片是url 调用示例如下
# result = aipOcr.basicGeneral('http://img0.ph.126.net/JgZPujjerZ1A7U_6gfs8Ag==/2515260391903843500.jpg')

# result = aipOcr.basicGeneral(
#     get_file_content(r'D:\demo\4_linxuewei_linbaliu\20140424_xuechanggui\2img.jpg'))
# result = aipOcr.tableRecognitionAsync(get_file_content(r'D:\demo\4_linxuewei_linbaliu\20110505_xuechanggui\1img.jpg'))
# # result = aipOcr.basicGeneral(get_file_content('e:/test/cropImg' + str(1) + '.jpg'))
# print(result)
mm=aipOcr.getTableRecognitionResult('10073324_17299', {
    'result_type': 'json',
})
print(mm)
# print(result['words_result'])
# for res in result['words_result']:
#     print(res['words'])

# with open('d:/pic.txt', 'r') as fp:
#     for line in fp.readlines():
#         path1, name = os.path.split(line.strip())
#         # print(os.path.exists(os.path.join(path1, 'result.txt')))
#         if not os.path.exists(os.path.join(path1, 'result.txt')):
#             sleep(1)
#             with open(os.path.join(path1, 'result.txt'), 'a', encoding='utf-8') as ff:
#                 result = aipOcr.basicGeneral(get_file_content(line.strip()))
#                 if result.get('words_result_num', 0) > 0:
#                     for res in result['words_result']:
#                         print(res['words'])
#                         ff.write(res['words'])
#                         ff.write('\n')
