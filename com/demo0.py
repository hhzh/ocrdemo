import os
import cv2
import ctypes
import numpy as np
import threading
from time import ctime, sleep
import datetime
import pypinyin

# filepath = 'E:/bak/dd.txt'
# filepath = filepath.replace('E:', 'D:')
# # print(filepath)
# paths,_=os.path.split(filepath)
# if not os.path.exists(paths):
#     os.mkdir(paths)
# with open(filepath, 'a') as fp:
#     fp.write('hello')

# 读取图片
# def get_file_content(filepath):
#     with open(filepath, 'rb') as fp:
#         return fp.read()
#
# afile = 'E:/6月3号御方堂/1_李子香_淋巴瘤_全/20170410_超声检查报告单.jpg'
# afile = 'E:\\6月3号御方堂\\10_艾晋华_横纹肌肉瘤\\1.png'
# afile = 'E:/crop/中文/22.jpg'
# # img=get_file_content(afile)
# # print(type(img))
# # img=np.array(img)
# # print(type(img))
#
# # afile = 'E:\\1.jpg'
# img = cv2.imread(afile)
# # cv2.imshow('Img',img)
# # cv2.waitKey(0)
# if type(img)==type(None):
#     print('hello')
# # if isinstance(img, ctypes.):
# #     print('hello')
# print(type(img))
# print(img.size)
# print(img.shape)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 删除文件
# def traverseRem(filepath):
#     files = os.listdir(filepath)
#     for fi in files:
#         fi_d = os.path.join(filepath, fi)
#         if os.path.isdir(fi_d):
#             traverseRem(fi_d)
#         elif fi_d.endswith('errorOcr.log') or fi_d.endswith('result.txt') or fi_d.endswith('nohup.log'):
#             print('remove:' + fi_d)
#             os.remove(fi_d)
#
#
# traverseRem('d:/demo')

# def begin_ocr(imgpaths):
#     print('线程开始：')
#     for imgpath in imgpaths:
#         sleep(1)
#         print(imgpath)
#
#
# def create_thread(imgpaths):
#     x = 0
#     splitpaths = []
#     splitsize = int(len(imgpaths) / 10)
#     while x < len(imgpaths):
#         splitpaths.append(imgpaths[x:x + splitsize])
#         x = x + splitsize
#     ths = []
#     for splitpath in splitpaths:
#         th = threading.Thread(target=begin_ocr, args=(splitpath,))
#         ths.append(th)
#     for i in ths:
#         i.start()
#     for i in ths:
#         i.join()
#
#
# if __name__ == '__main__':
#     aa = np.arange(1, 106)
#     create_thread(aa)

# aa = np.arange(53)
# x = 0
# bb = []
# xsize=int(int(53/5))
# while x < 53:
#     bb.append(aa[x:x + xsize])
#     x = x + xsize
#
# print(bb)
# for cc in bb:
#     print(cc)
# print(aa[50:60])

# with open('d:/error.txt', 'r',encoding='utf-8') as fp:
#     for line in fp.readlines():
#         if line.find('Connect') > 0:
#             print(line[line.index('error:') + 6:line.index('---')])

# aa = r"error:d:/demo\7_liutingfen_feiai_quan\20170124_bingqingjianjie1_qiluyiyuannanshanfenyuan\1img.jpg---cause:('Connection aborted.', OSError((-1, 'Unexpected EOF'),))"
# print(aa.index('Connect'))
# print(aa.find('Connect'))
# print(aa[aa.index('error:') + 6:aa.index('---')])

# img=cv2.imread('e:/da.png')
# print(img.shape)

# now = datetime.datetime.now()
# print(type(now))
# print(now)
# print(type(now.strftime('%Y-%m-%d %H:%M:%S')))
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
# filepath = '20170203-09jianyanbaogaodan（1）.jpg'
# print(filepath)
# filepath = filepath.replace('（', '(')
# filepath = filepath.replace('）', ')')
# fileen = pypinyin.slug(filepath, separator='')
# print(fileen)
# print('20170203-09jianyanbaogaodan(1).jpg')

# cv2.imdecode()
#
# paths = []
#
#
# def traverse(filepath):
#     files = os.listdir(filepath)
#     for fi in files:
#         fi_d = os.path.join(filepath, fi)
#         if os.path.isdir(fi_d):
#             traverse(fi_d)
#         else:
#             paths.append(os.path.join(filepath, fi_d))
#
#
# traverse('e:/55')
#
# for path in paths:
#     path1 = path.replace('（', '(')
#     path1 = path1.replace('）', ')')
#     print('----')
#     print(path)
#     print(path1)
#     os.rename(path, path1)

# filesize = os.path.getsize('e:/55/box.jpg') / 1024/1024
# xxx='{:.4f}'.format(filesize)
# print(type(xxx))
# print(xxx)
# print(type(filesize))
# print(filesize)

xx = np.array([[[671, 3921]], [[671, 3937]], [[670, 3938]]])
print(type(xx))
print(xx.shape)
print(xx[0][0][0])