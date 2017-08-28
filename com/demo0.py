import os
import cv2
import ctypes
import numpy as np

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
# afile = 'E:\\6月3号御方堂\\10_艾晋华_横纹肌肉瘤\\1.png'
# img=get_file_content(afile)
# print(type(img))
# img=np.array(img)
# print(type(img))

afile = 'E:\\1.jpg'
img = cv2.imread(afile)
# cv2.imshow('Img',img)
# cv2.waitKey(0)
if isinstance(img, ctypes.):
    print('hello')
print(type(img))
print(img.size)
print(img.shape)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
