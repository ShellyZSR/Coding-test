#7.2 文件的读写

#1 f.read(size=-1) 从文件中读入整个文件内容(括号中没有参数，默认返回整个文件）
f = open('/Users/teresa624/Documents/Coding/Python中文网课（淘宝凡博）/Python 编程+办公自动化（凡博网课）/上课随练code/第七章/7test.txt','r')
# a = f.read()
# print(a)
# a1 = f.read(10)  读取f文件的前10个字符
# print(a1)

#2 f.readline(size = -1)： 从文件中读入一行内容。(括号里为读取这一行的多少个字符）
# b = f.readline()
# print(b) #《秋登宣城谢眺北楼》返回第一行
# b1 = f.readline()
# print(b1) #李白 返回第二行
#
# b2 = f.readline(3)
# print(b2) #江城如 读取这一行的3个字符

#3 f.readlines(hint=-1)： 从文件中读入所有行，以每行为元素形成一个列表。
# 参数可选，如果给出，读入hint行。
# c = f.readlines()
# print(c)
#['《秋登宣城谢眺北楼》\n', '李白\n', '江城如画里,山晓望晴空。\n',
# '两水夹明镜,双桥落彩虹。\n', '人烟寒橘柚,秋色老梧桐。\n', '谁念北楼上,临风怀谢公。']
#\n 是代表回车，换行

c1 = f.readlines(1) #读取第一行
print(c1) #['《秋登宣城谢眺北楼》\n']
c2 = f.readlines(2)
print(c2) #['李白\n']
# c3 = f.readline()
# print(c3) #江城如画里,山晓望晴空。 (与下面代码对比一下）

##注意：文件打开后，对文件的读写有一个读取指针，上次读取之后到哪个位置，python会记住这个位置，下次会从这里接着往下读取

 #4 f.seek(offset)： 改变当前文件操作指针的位置，offset的值：0：文件开头； 2: 文件结尾
f.seek(0) #改变指针到文件开头
c3 = f.readline() #按行读取文件，读第一行
print(c3) #《秋登宣城谢眺北楼》

#5. 遍历循环for逐行遍历文件
f.seek(0)
for line in f:
    print(line,end="")

f.close()

#6. f.write(s)： 向文件写入字符串s，每次写入后，将会记录一个写入指针。
f1 = open('/Users/teresa624/Documents/Coding/Python中文网课（淘宝凡博）/Python 编程+办公自动化（凡博网课）/上课随练code/第七章/7.1test.txt','w')

# f1.write('《秋登宣城谢眺北楼》\n 李白')
# f1.close()

#7。 f.writelines(lines)：直接将列表类型的各元素连接起来写入文件f。
ls = ['《秋登宣城谢眺北楼》\n', '李白\n','江城如画里,山晓望晴空。\n','两水夹明镜,双桥落彩虹。\n']
f1.writelines(ls)
f1.close()