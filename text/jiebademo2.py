import sys
import jieba
import jieba.analyse
from optparse import OptionParser
import jieba.posseg as pseg

# words = pseg.cut("我爱北京天安门。")
# for w in words:
#     print("%s %s" % (w.word, w.flag))

# print('/'.join(jieba.cut('我来到北京清华大学', cut_all=False)))

with open(
        r'D:\6yue3haoyufangtang\1_lizixiang_linbaliu_quan\20170410_chaoshengjianchabaogaodan\result.txt',
        'r') as fp:
    for line in fp.readlines():
        # with open(
        #         r'D:\6yue3haoyufangtang\1_lizixiang_linbaliu_quan\20170410_zhuyuanbinganshouye1_jilindaxuedieryiyuan\cut.txt',
        #         'a') as ff:
        #     ff.write('/'.join(jieba.cut(line, cut_all=False)))
            print('/'.join(jieba.cut(line, cut_all=False)))
