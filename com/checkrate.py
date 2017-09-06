import os
import sys

path = r'd:\6yue3haoyufangtang'

nohup_num=0


# def traverse(filepath):
#     files = os.listdir(filepath)
#     exist_file = False
#     for file in files:
#         fi_d = os.path.join(filepath, file)
#         if os.path.isfile(fi_d) and file.endswith('nohup.txt'):
#             exist_file = True
#             nohup_num = nohup_num + 1
#
#     if exist_file:
#         for file in files:
#             fi_d = os.path.join(filepath, file)
#             if os.path.isfile(fi_d) and file.endswith('result.txt'):
#                 exist_file = True

def traverse(filepath):
    files = os.listdir(filepath)
    global nohup_num
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            traverse(fi_d)
        elif fi_d.endswith('result.txt'):
            nohup_num = nohup_num + 1


if __name__ == "__main__":
   traverse(path)
   print(nohup_num)