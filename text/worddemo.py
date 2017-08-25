import jieba


def get_file_content(filepath):
    with open(filepath, 'r') as fp:
        return fp.read()


content = get_file_content('e:/crop/result.txt')
seg_list = jieba.cut(content, cut_all=False)
print('/'.join(seg_list))
