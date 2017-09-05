import os
import sys

path = r'd:\6yue3haoyufangtang'

def traverse(filepath):
    files = os.listdir(filepath)
    for file in files:
        fi_d = os.path.join(filepath, file)
        print(fi_d)
