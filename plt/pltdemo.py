import matplotlib.pyplot as plt
import numpy as np

handle = []
ocr = []
# xtime = 0
xsec1 = 0
xsec2 = 0

handle.append(xsec1)
ocr.append(xsec2)

with open('e:/crop/ocr.txt', 'r') as fp:
    for line in fp.readlines():
        name, filesize, time = line.split('\t')
        hour, minute, second = time.split(':')
        # xtime = xtime + int(minute) * 60
        xsec1 = xsec1 + float(second)
        ocr.append(xsec1)
        # print(time)

with open('e:/crop/handle.txt', 'r') as fp:
    for line in fp.readlines():
        name,filesize, time = line.split('\t')
        hour, minute, second = time.split(':')
        # xtime = xtime + int(minute) * 60
        xsec2 = xsec2 + float(second)
        handle.append(xsec2)
        # print(time)
print(xsec1)
print(xsec2)
hx = np.arange(len(handle))
ox = np.arange(len(ocr))
plt.figure()
# plt.xlabel('图片个数/张')
# plt.ylabel('时间/秒')
l1, = plt.plot(hx, handle, c='r', label='image handle')
l2, = plt.plot(ox, ocr, c='b', label='baidu ocr')
plt.legend(handles=[l1, l2, ], labels=['image handle', 'baidu ocr'], loc='upper left')
# l1.annotate(xy=(364, 424), xytext=(+30, -30))
# l2.annotate(xy=(1545, 726), xytext=(+30, -30))
# plt.legend(handles=[l1, l2, ], labels=['aaa', 'bbb'], loc='upper right')
plt.show()
