import sys

sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser  # 引入关键词的包
from docopt import docopt

data_path = "d:/bbb.txt"
topK = 10
withWeight = False
content = "".join(open(data_path, 'r').read())  # print content
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)  # 直接调用

if withWeight is True:
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
else:
    print(",".join(tags))
