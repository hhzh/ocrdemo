import sys

sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

# USAGE = "usage:    python extract_tags.py [file name] -k [top k]"
#
# parser = OptionParser(USAGE)
# parser.add_option("-k", dest="topK")
# opt, args = parser.parse_args()
#
# print(opt)
# print(args)
#
# if len(args) < 1:
#     print(USAGE)
#     sys.exit(1)
#
# file_name = args[0]
#
# if opt.topK is None:
#     topK = 10
# else:
#     topK = int(opt.topK)
#
# content = open(file_name, 'rb').read()
#
# tags = jieba.analyse.extract_tags(content, topK=topK)
#
# print(",".join(tags))

MSG_USAGE = "myprog[ -f ][-s ] arg1[,arg2..]"
optParser = OptionParser(MSG_USAGE)
# 以上，产生一个OptionParser的物件optParser。传入的值MSG_USAGE可被调用打印命令时显示出来。

optParser.add_option("-f", "--file", action="store", type="string", dest="fileName")
optParser.add_option("-v", "--vison", action="store_false", dest="verbose", default='gggggg',
                     help="make lots of noise [default]")
# 调用OptionParser.add_option()添加选项，add_option()参数说明：
# action:存储方式，分为三种store, store_false, store_true
# type:类型
# dest:存储的变量
# default:默认值
# help:帮助信息

fakeArgs = ['-f', 'file.txt', '-v', 'good luck to you', 'arg2', 'arge']
options, args = optParser.parse_args(fakeArgs)
print(options.fileName)
print(options.verbose)
print(options)
print(args)
