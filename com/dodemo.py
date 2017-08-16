import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('e:/1.jpg')

# 边缘检测
edges = cv2.Canny(img, 100, 100)
# cv2.imshow('Image', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite('e:/edges.jpg', edges)
