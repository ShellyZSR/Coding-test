# 6.4 元组 tuple
lt = ('风清扬','令狐冲','东方不败','肖峰','东方不败')

#1 lt.count(x) 元素x在元组中一共有多少个
print(lt.count('东方不败')) #2

#2 lt.index(x) 对应参数x在元组中的索引名
print(lt.index('东方不败'))  #2
print(lt.index('令狐冲'))    #1

#3. tuple()
ls = ['风清扬','令狐冲','东方不败']
lt = tuple(ls)
print(lt,type(lt))
#('风清扬', '令狐冲', '东方不败') <class 'tuple'>
lp = "十大武林高手"
print(tuple(lp))
#('十', '大', '武', '林', '高', '手')

#4 sorted()
set1 = set('happy')
print(sorted(set1))
#['a', 'h', 'p', 'y']