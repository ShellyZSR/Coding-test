#6.3列表类型的操作
#1.s.append(x)
ls = ["东方不败",'杨过','风清扬','令狐冲']
ls.append('欧阳锋')
print(ls)

#ls.append(x)仅用于在列表中增加一个元素，
# 如果希望增加多个元素，可以使用加号+，将两个列表合并。
lt = ['肖峰','独孤求败']
ls += lt
print(ls)
# ['东方不败', '杨过', '风清扬', '令狐冲', '欧阳锋', '肖峰', '独孤求败']

#2. ls.insert(i, x) 在列表ls第i位置增加元素x
ls.insert(0,"晓梅")
print(ls)

# 3. ls.clear() 删除列表ls中所有元素
lt.clear()
print(lt)
# [] 代表空列表

#4. ls.pop(i) 将列表ls中第i项元素取出并删除该元素
print(ls.pop(0)) #晓梅 （取出并输出第i项元素）
print(ls) #（删除该元素）

#5. ls.remove(x) 将列表中出现的第一个元素x删除
ls.append("东方不败")
print(ls) #['东方不败', '杨过', '风清扬', '令狐冲', '欧阳锋', '肖峰', '独孤求败', '东方不败']
ls.remove("东方不败") #第一个"东方不败"删掉
print(ls) #['杨过', '风清扬', '令狐冲', '欧阳锋', '肖峰', '独孤求败', '东方不败']

#6。 ls.reverse() 将列表ls中元素反转
print(ls.reverse()) #None 此项操作不会返回任何数据，而是直接操作这个列表
print(ls) #['东方不败', '独孤求败', '肖峰', '欧阳锋', '令狐冲', '风清扬', '杨过'] 已reverse

#6。 ls.copy() 生成一个新列表，复制ls中所有元素
lm = ls.copy()
print(lm)
#此项操作会重新开辟一个空间,复制ls给lm，计算机会给lm一个新的编号，
# 这时对ls进行操作，将不会干扰影响到lm，ls.clear()之后，lm也不会被clear.(但lm = ls会被ls影响）

#7. del列表变量[索引序列] 可以使用Python保留字del对列表元素或片段进行删除
del lm[2]
print(lm)
print("end")

del lm[0:2]
print(lm)

#8 使用索引配合等号（=）可以对列表元素进行修改。
ls1 = ["a","b","c","d"]
ls1[2] = 'm'
print(ls1)
#输出：['a', 'b', 'm', 'd']