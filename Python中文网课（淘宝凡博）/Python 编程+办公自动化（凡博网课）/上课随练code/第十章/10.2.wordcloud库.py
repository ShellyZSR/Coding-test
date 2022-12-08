#10.2 wordcloud库
#例1：
# import wordcloud
# txt = 'Python is a little bit difficult,but I like Python and I am learning it now.'
# wd = wordcloud.WordCloud().generate(txt)
# wd.to_file('Wdtest.png')

#例2：中文词云
# import jieba
# import wordcloud
# txt1 = 'Python由荷兰数学和计算机科学研究学会的吉多·范罗苏姆 于1990 年代初设计。\
# Python提供了高效的高级数据结构，还能简单有效地面向对象编程。'
# words = jieba.lcut(txt1) #精确分词
# newtxt1 = ' '.join(words) #用空格连接
# print(newtxt1)
# wd1 = wordcloud.WordCloud(font_path="msyh.ttc",width=500,height=500).generate(newtxt1)
# wd1.to_file('中文词云图例子1.png')

#例3：生成文件词云
import wordcloud
with open ('Essay词云.txt','r') as file:
    text2 = file.read()
    wd2 = wordcloud.WordCloud(background_color="white",\
                             width=800,\
                             height=600,\
                             max_words=100,\
                             max_font_size=80,\
                             ).generate(text2)
    wd2.to_file('Essay词云.png')