#4.3循环结构
#4.3.1遍历循环
#遍历结构是字符串：可以逐一遍历字符串里的每个字符
for c in 'Python':
    print(c)

print("end")

#遍历结构是range()函数：可指定语句块的循环次数  range(start,stop,step)
for x in range(3,11,2):
    print(x)
print('end1')
# 输出为：
# 3
# 5
# 7
# 9
# end

#break用法

for z in 'range':
    if z == 'n':
        break
    print(z)

print("end")

#continue用法

for z in range(10):
    if z == 2 or z == 3: #2,3被跳过了
        continue
    print(z)

print("end")

#遍历循环扩展模式for-else：
# 当for循环正常执行之后，程序会继续执行else语句中的程序
# 1
for c in "python":
    if c == "t":
        break  #当c==t时break，for循环非正常结束
    print(c)
else:          #else语句将不会被执行
    print('循环正常结束')
print('end')
# 2
for c in "python":
    if c == "t":
        continue     #当c==t时continue，结束当次循环并继续执行后面循环，for循环会正常结束
    print(c)
else:              #else语句将被执行  
    print('循环正常结束')
print('end')



#嵌套循环（两个/多个for),先走最内层for循环，当这层for循环结束，再走外面一层
#的循环，以此类推。
for i in range(1,3):
    print('第{}次循环：'.format(i))
    for j in range(1,3):
        print("\t第{}次循环内部的第{}次循环：{}*{}={}".format(i,j,i,j,i*j))
print('循环结束')
# 第1次循环：
# 	第1次循环内部的第1次循环：1*1=1
# 	第1次循环内部的第2次循环：1*2=2
# 第2次循环：
# 	第2次循环内部的第1次循环：2*1=2
# 	第2次循环内部的第2次循环：2*2=4
# 循环结束