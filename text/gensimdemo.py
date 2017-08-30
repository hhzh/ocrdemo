from gensim.models import word2vec
from gensim.models import Word2Vec
import gensim
from gensim.models.word2vec import LineSentence
import jieba
import multiprocessing

# def generateTrainedModel(filename, num):
#     output = open(filename, 'w')
#     count = 0
#     content = str(num) + ' 200\n'
#     for k, v in model.vocab.items():
#         # print k,type(model[k].tolist())
#         l = (model[k].tolist())
#         content += str(k) + ' '
#         for i in l:
#             content += str(i) + ' '
#         for i in l[:-1]:
#             content += str(i) + ' '
#         content += str(l[-1])
#         content += '\n'
#     # content.encode('utf-8')
#     output.write(content[:-2])
#     output.close()

# sentences = [['first', 'sentence'], ['second', 'sentence']]
# # train word2vec on the two sentences
# model = gensim.models.Word2Vec(sentences, min_count=1)

# with open('d:/ba.txt', encoding='gbk', errors='ignore') as fp:
#     lines = fp.readlines()
#     for line in lines:
#         line.replace('\t', '').replace('\n', '').replace(' ', '')
#         seg_list = jieba.cut(line, cut_all=False)
#         with open('d:/result.txt', 'a', encoding='gbk') as ff:
#             ff.write(" ".join(seg_list))

# sentences =Word2Vec.Text(u"fenci_result.txt")  # 加载语料
# model =word2vec.Word2Vec(sentences, size=200)  #训练skip-gram模型，默认window=5

# model = gensim.models.Word2Vec.load('d:/result.txt')
# model = gensim.models.KeyedVectors.load_word2vec_format('d:/05.txt', encoding='gbk', binary=True)

# model = Word2Vec(LineSentence('d:/result.txt'), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())

# sentences = word2vec.Text8Corpus(u'd:/result.txt')
# model = word2vec.Word2Vec(sentences, size=200)
#
# print(model.similarity('him', 'I'))

# text_list = []
# with open('d:/dd.txt', 'r',encoding='utf8') as fread:
#     for line in fread.readlines():
#         # if line_num> 100:
#         #     break
#         seg_list = jieba.cut(str(line), cut_all=False)
#         word_list = [item for item in seg_list if len(item) > 1]
#         text_list.append(word_list)
#
# w2v_model = Word2Vec(text_list)
# w2v_model.save('d:/bb.model')

# text_list = segment_novel('./data/gulong.txt','gulong_dict2.txt')
out_model_file = 'd:/bb.model'
# train_word2vec(text_list,out_model_file)
model = Word2Vec.load(out_model_file)
for e in model.most_similar(positive=[u'慕容复'], topn=30):
    print(e[0], e[1])
