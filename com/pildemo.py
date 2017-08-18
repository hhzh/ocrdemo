# from PIL import Image, ImageFilter
import cv2
import numpy
import os

#
# img = Image.open('e:/1.jpg')
# w, h = img.size
# print(w, h)
# # img2=img.filter(ImageFilter.BLUR)
# img.thumbnail((2000 * w / h, 2000))
# img.save('e:/copy1.jpg')
# # img.load()

# # img.show()

# img = cv2.imread('e:/test1')
# print(img)
# randomByteArray = bytearray(os.urandom(120000))
# flatNumpyArray = numpy.arange(randomByteArray)
flatNumpyArray = numpy.random.randint(0, 256, 120000)
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage)
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage)
print(bgrImage)