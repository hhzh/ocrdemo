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

# with open('d:/天龙八部.txt', errors='ignore', encoding='utf-8') as fp:
#     lines = fp.readlines()
#     for line in lines:
#         seg_list = jieba.cut(line)
#         with open('d:/分词后的天龙八部.txt', 'a', encoding='utf-8') as ff:
#             ff.write(' '.join(seg_list))

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
# out_model_file = 'd:/bb.model'
# # train_word2vec(text_list,out_model_file)
# model = Word2Vec.load(out_model_file)
# # for e in model.most_similar(positive=[u'童姥'], topn=30):
# #     print(e[0], e[1])
# print(model.similarity(u'乔峰', u'李秋水'))

# 加载语料
sentences = word2vec.Text8Corpus('d:/分词后的天龙八部.txt')

# 训练模型
model = word2vec.Word2Vec(sentences)

# # 选出最相似的10个词
# for e in model.most_similar(positive=['乔峰'], topn=30):
#     print(e[0], e[1])
#
# # 保存模型
# model.save('d:/天龙八部.model')
#
# # 加载模型
# model = word2vec.Word2Vec.load('d:/天龙八部.model')
#
# model.save_word2vec_format('d:/天龙八部.model.bin', binary=True)
# model = word2vec.Word2Vec.load_word2vec_format('d:/天龙八部.model.bin', binary=True)
#
# 计算两个词的相似度
print(model.similarity('乔峰', '慕容复'))

# 计算两个集合的相似度
list1 = ['乔峰', '慕容复']
list2 = ['萧远山', '慕容博']
print(model.n_similarity(list1, list2))

# 选出集合中不同类的词语
list3 = ['乔峰', '段誉', '虚竹', '丁春秋']
print(model.doesnt_match(list3))

# # 查看词的向量值
# print(type(model['乔峰']))  # 输出 <class 'numpy.ndarray'>
# print(len(model['乔峰']))  # 输出 100
# print(model['乔峰'])  # 输出 一行100列的向量

