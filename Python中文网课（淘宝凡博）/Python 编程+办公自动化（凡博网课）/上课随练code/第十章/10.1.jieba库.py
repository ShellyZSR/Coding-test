#10.1 jieba库
import jieba
#1. jieba.lcut(s) 是最常见的中文分词函数，用于精准模式，即将字符串分割成等量的中文词组，返回结果是列表类型。
print(jieba.lcut("由于中文文本中的单词不是通过空格或者标点符号分隔"))

#2. jieba.lcut(s,cut_all = True)用于全模式：即将字符串的所有分词可能均列出来，返回结果是列表类型，冗余性大
print(jieba.lcut("由于中文文本中的单词不是通过空格或者标点符号分隔",cut_all = True))

#3. jieba.lcut_for_search(s)返回搜索引擎模式：该模式首先执行精确模式，然后再对其中长词进一步切分，
# 再获得最终结果。
print(jieba._lcut_for_search("由于中文文本中的单词不是通过空格或者标点符号分隔"))

#4. jieba.add_word(): 用于向jieba词库增加新的单词
print(jieba.lcut('潮享享教育')) #输出：['潮', '享享', '教育']
jieba.add_word("潮享")
print(jieba.lcut('潮享教育')) #['潮享', '教育']