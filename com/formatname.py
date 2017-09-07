import os
paths = []


def traverse(filepath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            traverse(fi_d)
        else:
            paths.append(os.path.join(filepath, fi_d))


traverse(r'E:\6yue3haoyufangtang')

for path in paths:
    path1 = path.replace('（', '(')
    path1 = path1.replace('）', ')')
    path1 = path1.replace('、', '[')
    path1 = path1.replace('【', '[')
    path1 = path1.replace('】', ']')
    # path1 = path1.replace('?', '0')
    print('----')
    print(path)
    print(path1)
    os.rename(path, path1)