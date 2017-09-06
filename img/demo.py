import cv2
import os
from time import ctime
import datetime

# # img=cv2.imread(r'E:\github\ocrdemo\img\img.jpg')
# img=cv2.imread(r'd:/timg.jpg')
# print(type(img))
# print(len(img))
# cv2.imshow('img',img)
# cv2.waitKey(0)

# print(os.path.join(os.path.abspath('./img'), 'img.jpg'))

# result = ''
# with open('e:/66/result0.txt', 'r', encoding='utf-8') as fp:
#     for line in fp.readlines():
#         result = result + line
# print(result)

# result = ''
# with open(os.path.join(os.path.abspath('./img/fdf6abbf438e8de090bd6400294621d2'), 'result.txt'), 'r',
#           encoding='utf-8') as fp:
#     for line in fp.readlines():
#         result = result + line
# print(result)

print(ctime())
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
