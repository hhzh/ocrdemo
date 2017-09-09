import numpy as np

handle = []
ocr = []
errors = []
# xtime = 0
xsec1 = 0
xsec2 = 0

handle.append(xsec1)
ocr.append(xsec2)

# with open('e:/crop/handleRes.txt', 'a') as fp:
#     with open('e:/crop/handle.txt', 'r') as ff:
#         for line in ff.readlines():
#             fp.write(line.strip() + '\t' + 'success')
#             fp.write('\n')
# for line in fp.readlines():
#     name, time = line.split('\t')
#     hour, minute, second = time.split(':')
#     # xtime = xtime + int(minute) * 60
#     xsec2 = xsec2 + float(second)
#     handle.append(xsec2)
#     # print(time)

with open('e:/crop/errorOcr.log', 'r') as fp:
    for line in fp.readlines():
        name, error = line.split('---')
        errors.append(name)
with open('e:/crop/ocrRes.txt', 'a') as ff:
    with open('e:/crop/ocr.txt', 'r') as fp:
        for line in fp.readlines():
            name, _, xxx = line.split('\t')
            if name in errors:
                ff.write(line.strip() + '\t' + 'emptyImage')
            else:
                ff.write(line.strip() + '\t' + 'success')
            ff.write('\n')
