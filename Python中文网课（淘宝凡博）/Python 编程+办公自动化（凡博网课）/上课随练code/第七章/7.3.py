# 7.3 数据的维度

# #1。 join()函数：方法用于将序列中的元素以指定的字符连接生成一个新的字符串
# ls = ['Beijing','London','Paris','Roma','Milan']
# f = open('/Users/teresa624/Documents/Coding/Python中文网课（淘宝凡博）/Python 编程+办公自动化（凡博网课）/上课随练code/第七章/City.txt','w')
# f.write('\n'.join(ls))
# f.close

#2. ().csv格式文件,可以直接被Excel读取识别，每个元素是表格里的一个内容（一个格子一个元素）
# ls = ['Beijing','London','Paris','Roma','Milan']
# f = open('/Users/teresa624/Documents/Coding/Python中文网课（淘宝凡博）/Python 编程+办公自动化（凡博网课）/上课随练code/第七章/City.csv','w')
# f.write(','.join(ls))
# f.close

#3 ls.split("x")：通过指定分隔符x，对字符串进行切片，并返回列表
f = open('上课随练code/第七章/City.csv','r')
ls = f.read()
print(ls,type(ls)) 
#Beijing,London,Paris,Roma,Milan <class 'str'>
ls_new = ls.split(",")   #通过逗号','，对字符串ls进行分隔，并返回列表
print(ls_new) 
#['Beijing', 'London', 'Paris', 'Roma', 'Milan']
print(type(ls_new)) 
#<class 'list'>