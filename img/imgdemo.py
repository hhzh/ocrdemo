import matplotlib.pyplot as plt
import numpy as np

f = open(r'D:\demo\4_linxuewei_linbaliu\20110505_xuechanggui\1img.jpg', mode='rb')
# x = np.fromfile(f, dtype=np.ubyte)
# print(type(x))
# print(len(x))
# # #x = x[0:1920]
# # x = x[1920:3840]
# # #x = x[3840:5760]
# # x = x.reshape(60,32)
# # #print((x))
# # plt.imshow(x)
# # plt.axis('off')  # clear x- and y-axes
# # plt.show()

xx = f.read()
# with open('img.txt', 'w') as fp:
#     fp.write(str(xx))
# print(type(xx))
# print(len(xx))
# print(xx)
print(xx.decode('utf-8'))
f.close()
