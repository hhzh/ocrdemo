import cv2
import numpy as np
import os
import pypinyin

paths = []


def traverse(filepath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            traverse(fi_d)
        else:
            paths.append(os.path.join(filepath, fi_d))


traverse('E:\\6月3号御方堂')
for afile in paths:
    if afile.endswith('.JPG') or afile.endswith('.jpg') or afile.endswith('.JPEG') or afile.endswith(
            '.PNG') or afile.endswith('.png'):
        filepath, filename = os.path.split(afile)
        # filepath = filepath.replace('E:', 'D:')
        filepathEn = pypinyin.slug(filepath, separator='')
        if not os.path.exists(filepathEn):
            # print(filepathEn)
            os.makedirs(filepathEn)
        with open(afile, 'rb') as ff:
            respath = os.path.join(filepathEn, pypinyin.slug(filename, separator=''))
            print(respath)
            try:
                with open(respath, 'wb') as fp:
                    readimg = ff.read()
                    fp.write(readimg)
            except:
                print('error:' + respath)

                # print(afile)
                # img = cv2.imread(afile)
                #
                # try:
                #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #     edges = cv2.Canny(gray, 100, 300, apertureSize=3)
                #
                #     # blur and threshold the image
                #     blurred = cv2.blur(edges, (11, 11))
                #     (_, thresh) = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY)
                #
                #     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (300, 300))
                #     closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
                #
                #     # perform a series of erosions and dilations
                #     closed = cv2.erode(closed, None, iterations=4)
                #     closed = cv2.dilate(closed, None, iterations=4)
                #
                #     image, contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                #     c = sorted(contours, key=cv2.contourArea, reverse=True)
                #
                #     for cc in c:
                #         # compute the rotated bounding box of the largest contour
                #         rect = cv2.minAreaRect(cc)
                #         box = np.int0(cv2.boxPoints(rect))
                #
                #         Xs = [i[0] for i in box]
                #         Ys = [i[1] for i in box]
                #         x1 = min(Xs) - 15
                #         x2 = max(Xs) + 15
                #         y1 = min(Ys) - 15
                #         y2 = max(Ys) + 15
                #         height = y2 - y1
                #         width = x2 - x1
                #         cropImg = img[y1:y1 + height, x1:x1 + width]
                #         # draw a bounding box arounded the detected barcode and display the image
                #         cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
                #
                #         cv2.imwrite(filepath + 'cropImg' + str(mm) + '.jpg', cropImg)
                #         mm = mm + 1
                #     cv2.imwrite(os.path.join(filepath, filename), img)
                # except:
                #     print("error.")
