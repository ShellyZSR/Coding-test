#6.2 list列表类型
# 1. list(x)将集合或字符串转化为列表类型
a = "列表可以由字符串构成"
print(list(a))

b = {"def","def", 123,234,12,23.4,23.4,879,"123"}
c = list(b)
print(c,type(c))

#2 序列类型通用的操作符和函数

#(1)列表的索引
ls = [1010,"1010",[1010,"1022"],'list'] #list里套list,其中list整体算一个元素
print(ls[3]) #list
print(ls[-2]) #[1010, '1022']
print('end')
#print(ls[5]) #报错：IndexError: list index out of range

#(2)list-遍历循环
ls1 = [1010,"1010",[1010,"1022"],'list']
for i in ls1:
    i = i * 2
    print(i)
#输出结果：
# 2020
# 10101010
# [1010, '1022', 1010, '1022']
# listlist

#(3)list-列表的切片
ls2 = [1010,"1011",[1010,1011],1012]
print(ls2[1:4]) # ls[N:M:K] 从第N位到第M位，不包含M，步长位K
print(ls2[-3:-1])
print(ls2[0:4:2])