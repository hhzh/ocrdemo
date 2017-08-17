import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('e:/done/houghline.jpg')

# 腐蚀 膨胀 开运算 闭运算
# # img = cv2.GaussianBlur(img, (3, 3), 0)
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # edges = cv2.Canny(gray, 50, 150, apertureSize=3)
# kernel = np.ones((1, 1), np.uint8)
# # erosion = cv2.erode(img, kernel, iterations=1)
# # dilation = cv2.dilate(img,kernel,iterations = 1)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# # closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# # gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# # tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# # blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
# # plt.subplot(121), plt.imshow(opening), plt.title('Original')
# # plt.xticks([]), plt.yticks([])
# # # plt.subplot(122), plt.imshow(opening), plt.title('Blurred')
# # # plt.xticks([]), plt.yticks([])
# # plt.show()
#
# cv2.imwrite('e:/demo/opening.jpg', opening)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# step2
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

# step3
# blur and threshold the image
blurred = cv2.blur(gradient, (15, 15))
(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

# step4
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
# closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)


# 霍夫直线
# img = cv2.GaussianBlur(img, (3, 3), 0)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(thresh, 50, 150, apertureSize=3)
# lines = cv2.HoughLines(thresh, 1, np.pi / 180, 800)
# for line in lines:
#     for rho, theta in lines[0]:
#         print(rho, theta)
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         x1 = int(x0 + 1000 * (-b))
#         y1 = int(y0 + 1000 * (a))
#         x2 = int(x0 - 1000 * (-b))
#         y2 = int(y0 - 1000 * (a))
#         cv2.line(thresh, (x1, y1), (x2, y2), (0, 0, 0), 2)
#
# cv2.imwrite('e:/demo/houghline.jpg', img)
# cv2.imwrite('e:/demo/edges.jpg', edges)
# print(type(lines))
# print(lines)

cv2.imwrite('e:/done/thresh.jpg', thresh)
