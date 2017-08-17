import numpy as np
import cv2
from matplotlib import pyplot as plt

# from PIL import Image
# print(numpy.arange(1,10))

img = cv2.imread('e:/2.jpg')
# cv2.namedWindow("Image")
# cv2.imshow('Image', image)
# k = cv2.waitKey(0)
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('cats.jpg', image)
#     cv2.destroyAllWindows()
# cv.imwrite('d:/da.png', image)
# print(cv2.__version__)

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])
# plt.show()

# px = img[100, 100]
# print(px)
# blue = img[100, 100, 0]
# print(blue)
# img[100, 100] = [255, 255, 255]
# print(img[100, 100])
# cv2.namedWindow("Image")
# cv2.imshow('Image', img)
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(img.shape)
# print(img.size)
# print(img.dtype)

# ball=img[280:340,330:390]
# img[273:333,100:160]=ball
# cv2.namedWindow("Image")
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# b, g, r = cv2.split(img)
# print(b,g,r)
# img = cv2.merge((b, g, r))
# img[:, :, 2] = 0
# cv2.namedWindow("Image")
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# e1 = cv2.getTickCount()
# for i in np.xrange(5, 49, 2):
#     img = cv2.medianBlur(img, i)
# e2 = cv2.getTickCount()
# t = (e2 - e1) / cv2.getTickFrequency()
# print(t)

# print(cv2.useOptimized())

# flags=[i for dir(cv2) if i.startswith('COLOR_')]
# print(flags)

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower_blue = np.array([110, 50, 50])
# upper_blue = np.array([130, 255, 255])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
# res = cv2.bitwise_and(img, img, mask=mask)
#
# cv2.imshow('img', img)
# cv2.imshow('mask', mask)
# cv2.imshow('res', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# green = np.uint8([[[0, 255, 0]]])
# hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
# print(hsv_green)

# res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# height, width = img.shape[:2]
# res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
# cv2.imshow('res', res)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 旋转变换
# rows, cols, _ = img.shape
# M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.6)
# dst = cv2.warpAffine(img, M, (2 * cols, 2 * rows))
# cv2.imshow('IMG', img)
# cv2.imshow('img', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 仿射变换
# rows, cols, ch = img.shape
# pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
# M = cv2.getAffineTransform(pts1, pts2)
# dst = cv2.warpAffine(img, M, (cols, rows))
# plt.subplot(1, 2, 1)
# plt.imshow(img)
# plt.title('Input')
# plt.subplot(1, 2, 2)
# plt.imshow(dst)
# plt.title('Output')
# # plt.subplot(121, plt.imshow(img), plt.title('Input'))
# # plt.subplot(122, plt.imshow(img), plt.title('Output'))
# plt.show()

# 透视变换
# rows, cols, ch = img.shape
# pts1 = np.float32([[395, 951], [3142, 840], [425, 4183], [3168, 4255]])
# pts2 = np.float32([[0, 0], [3312, 0], [0, 4416], [3312, 4416]])
# M = cv2.getPerspectiveTransform(pts1, pts2)
# dst = cv2.warpPerspective(img, M, (3312, 4416))
# # cv2.imshow('res', img)
# # cv2.waitKeyEx(0)
# # cv2.destroyAllWindows()
# # plt.subplot(121)
# # plt.title('Input')
# # plt.imshow(img)
# # plt.subplot(122)
# # plt.imshow(dst)
# # plt.title('Output')
# # # plt.subplot(121, plt.imshow(img), plt.title('Input'))
# # # plt.subplot(121, plt.imshow(dst), plt.title('Output'))
# # plt.show()
# cv2.imwrite('e:/demo/demo.jpg', dst)

# 阈值化
# ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in np.arange(0, 5):
#     plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()

# 自适应阈值
# img = cv2.medianBlur(img, 1)
# ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# titles = ['Original Image', 'Global Thresholding (v=127)', 'Adaptive Mean Thresholding',
#           'Adaptive Gaussian Thresholding']
# # images = [img, th1, th2, th3]
# # for i in np.arange(0, 4):
# #     plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
# #     plt.title(titles[i])
# #     plt.xticks([]), plt.yticks([])
# # plt.show()
# cv2.imwrite('e:/demo/thresh.jpg',th3)

# OTSU 二值化
# ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# blur = cv2.GaussianBlur(img, (5, 5), 0)
# ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# images = [img, 0, th1, img, 0, th2, img, 0, th3]
# titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)', 'Original Noisy Image',
#           'Histogram', "Otsu's Thresholding", 'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
# for i in np.arange(0, 3):
#     plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
#     plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
#     plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
#     plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
#     plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks()
# plt.show()

# 2D卷积
# kernel = np.ones((5, 5), np.float32) / 25
# dst = cv2.filter2D(img, -1, kernel)
# plt.subplot(121), plt.imshow(img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()

# 平均滤波
# blur = cv2.blur(img, (5, 5))
# # 0 是指根据窗口大小（ 5,5 ）来计算高斯函数标准差
# # blur = cv2.GaussianBlur(img, (5, 5), 0)
# # blur = cv2.medianBlur(img, 5)
# # blur = cv2.bilateralFilter(img, 9, 75, 75)
# plt.subplot(121), plt.imshow(img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

# 腐蚀 膨胀 开运算 闭运算
# # img = cv2.GaussianBlur(img, (3, 3), 0)
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # edges = cv2.Canny(gray, 50, 150, apertureSize=3)
# kernel = np.ones((3, 3), np.uint8)
# # erosion = cv2.erode(img, kernel, iterations=1)
# # dilation = cv2.dilate(img,kernel,iterations = 1)
# # opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# # closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# # gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# # tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# # blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
# plt.subplot(121), plt.imshow(img), plt.title('Original')
# plt.xticks([]), plt.yticks([])
# # plt.subplot(122), plt.imshow(opening), plt.title('Blurred')
# # plt.xticks([]), plt.yticks([])
# plt.show()

# 图像梯度
# # cv2.CV_64F 输出图像的深度（数据类型），可以使用 -1, 与原图像保持一致 np.uint8
# laplacian = cv2.Laplacian(img, cv2.CV_64F)
# # 参数 1,0 为只在 x 方向求一阶导数，最大可以求 2 阶导数。
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# # 参数 0,1 为只在 y 方向求一阶导数，最大可以求 2 阶导数。
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# plt.show()

# # Output dtype = cv2.CV_8U
# sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
# # 也可以将参数设为 -1
# # sobelx8u = cv2.Sobel(img,-1,1,0,ksize=5)
# # Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
# sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# abs_sobel64f = np.absolute(sobelx64f)
# sobel_8u = np.uint8(abs_sobel64f)
# plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
# plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
# plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
# plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
# plt.show()

# 边缘检测
# edges = cv2.Canny(img, 50, 100)
# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(edges, cmap='gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()

# 轮廓
# imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # print(image)
# print(contours)
# print(hierarchy)

# 直方图均衡化
# equ = cv2.equalizeHist(img)
# res = np.hstack((img, equ))
# # stacking images side-by-side
# # cv2.imwrite('res.png',res)
# cv2.imshow('res', res)
# cv2.waitKeyEx(0)
# cv2.destroyAllWindows()

# 霍夫直线
# img = cv2.GaussianBlur(img, (3, 3), 0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 400, 500, apertureSize=3)
# lines = cv2.HoughLines(edges, 1, np.pi / 180, 425)
# for line in lines:
#     for rho, theta in line:
#         print(rho, theta)
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         x1 = int(x0 + 1000 * (-b))
#         y1 = int(y0 + 1000 * (a))
#         x2 = int(x0 - 3000 * (-b))
#         y2 = int(y0 - 3000 * (a))
#         cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)

# blur and threshold the image
blurred = cv2.blur(edges, (7, 7))
(_, thresh) = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (100, 100))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# perform a series of erosions and dilations
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)

image, contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = sorted(contours, key=cv2.contourArea, reverse=True)

for cc in c:
    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(cc)
    box = np.int0(cv2.boxPoints(rect))

    # draw a bounding box arounded the detected barcode and display the image
    cv2.drawContours(img, [box], -1, (0, 255, 0), 3)


# cv2.imshow("Image", img)
# cv2.imwrite("contoursImage2.jpg", img)
# cv2.waitKey(0)

cv2.imwrite('e:/demo/img.jpg', img)
cv2.imwrite('e:/demo/image.jpg', image)
print(type(hierarchy))
print(hierarchy)
# cv2.imwrite('e:/demo/edges.jpg', edges)
# print(type(lines))
# print(lines)

# 霍夫直线（改进版）
# for i in np.arange(5):
#     gray = cv2.GaussianBlur(img, (3, 3), 0)
#     edges = cv2.Canny(gray, 50, 150, apertureSize=3)
#     lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 500, 800)
#     # lines = cv2.HoughLines(edges, 1, np.pi / 180, 600)
#     # for line in lines:
#     #     for rho, theta in line:
#     #         print(rho, theta)
#     #         a = np.cos(theta)
#     #         b = np.sin(theta)
#     #         x0 = a * rho
#     #         y0 = b * rho
#     #         x1 = int(x0 + 1000 * (-b))
#     #         y1 = int(y0 + 1000 * (a))
#     #         x2 = int(x0 - 3000 * (-b))
#     #         y2 = int(y0 - 3000 * (a))
#     #         cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
#     for line in lines:
#         for x1, y1, x2, y2 in line:
#             cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
#             cv2.imwrite('e:/demo/houghline.jpg', img)
# cv2.imwrite('e:/demo/edges.jpg', edges)
