import cv2
import numpy as np
import os
import datetime

paths = []


def traverse(filepath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            traverse(fi_d)
        else:
            paths.append(os.path.join(filepath, fi_d))


sss = datetime.datetime.now()
traverse('/home/huazhen/file/6yue3haoyufangtang')
print('len(paths)=' + str(len(paths)))
for afile in paths:
    start = datetime.datetime.now()

    filepath, filename = os.path.split(afile)

    # filepath = filepath.replace('\\', '/')
    # print(filepath)
    # print(filename)
    # print(afile)

    xpath = os.path.join(filepath, os.path.splitext(filename)[0])
    # print(xpath)
    if not os.path.exists(xpath):
        os.makedirs(xpath)

    img = cv2.imread(os.path.join(filepath, filename))

    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 300, apertureSize=3)

        # blur and threshold the image
        blurred = cv2.blur(edges, (11, 11))
        (_, thresh) = cv2.threshold(blurred, 70, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (300, 300))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # perform a series of erosions and dilations
        closed = cv2.erode(closed, None, iterations=4)
        closed = cv2.dilate(closed, None, iterations=4)

        image, contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        c = sorted(contours, key=cv2.contourArea, reverse=True)

        mm = 1
        for cc in c:
            # compute the rotated bounding box of the largest contour
            rect = cv2.minAreaRect(cc)
            box = np.int0(cv2.boxPoints(rect))

            Xs = [i[0] for i in box]
            Ys = [i[1] for i in box]
            x1 = min(Xs) - 15
            x2 = max(Xs) + 15
            y1 = min(Ys) - 15
            y2 = max(Ys) + 15
            height = y2 - y1
            width = x2 - x1
            cropImg = img[y1:y1 + height, x1:x1 + width]

            cv2.imwrite(xpath + '/' + str(mm) + 'img.jpg', cropImg)

            cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
            mm = mm + 1
            # cv2.imwrite(os.path.join(xpath, 'zresult.jpg'), img)

    except Exception as e:
        with open('errorImg.log', 'a') as fp:
            fp.write(afile + '---' + str(e))
            fp.write('\n')
        print("error:" + afile)
    finally:
        end = datetime.datetime.now()
        with open('handle.txt', 'a') as fp:
            filesize = os.path.getsize(afile) / 1024 / 1024
            xxx = '{:.4f}'.format(filesize)
            fp.write(afile)
            fp.write('\t')
            fp.write(xxx)
            fp.write('\t')
            fp.write(str(end - start))
            fp.write('\n')
eee = datetime.datetime.now()
print(eee - sss)
with open('handle.txt', 'a') as fp:
    fp.write('------')
    fp.write(str(eee - sss))
    fp.write('\n')
    fp.write(str(len(paths)))
    fp.write('\n')
