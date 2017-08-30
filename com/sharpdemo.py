import cv2
import numpy as np

imgs = []
for i in np.arange(1, 7):
    img = cv2.imread('e:/test/demo3/' + str(i) + '.JPG')
    imgs.append(img)

for img in imgs:
    img = cv2.imread('e:/test/demo3/' + str(i) + '.JPG')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    print(fm)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgSoble = cv2.Sobel(gray, cv2.CV_16U, 1, 1)
# meanVal=np.mean(imgSoble[0])
# print(meanVal)
# print(type(imgSoble))
# print(imgSoble.shape)

# fm = cv2.Laplacian(gray, cv2.CV_64F).var()
# text = 'Not Blurry'

# if fm < 200:
#     text = 'Blurry'
# cv2.putText(img, '{}:{:.2f}'.format(text, fm), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
#
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# print(type(fm))
# print(fm)
