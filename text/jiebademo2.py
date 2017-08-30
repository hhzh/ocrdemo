import sys
import jieba
import jieba.analyse
from optparse import OptionParser
import jieba.posseg as pseg


words = pseg.cut("我爱北京天安门。")
for w in words:
    print("%s %s" %(w.word, w.flag))

