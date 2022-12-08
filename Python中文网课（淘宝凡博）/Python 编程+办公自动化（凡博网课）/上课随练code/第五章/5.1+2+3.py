#5.1 函数的基本使用

#1.简单函数
def fact_1():
    for i in range(5):
        print('我走在康庄大道，明亮，激昂')
fact_1() #只定义函数时，Python是不会运行函数里面的函数体的，只有调用这个函数时，才会运行。

#调用整数阶乘的函数
def fact_2(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s #相当于把 s 给 fact_2(4)
a = fact_2(4) #()里4的意思：将4赋值给参数n，调用函数fact_2此时n = 4.
print(a)
b = fact_2(3)
print(b)

#5.2 return语句

# 1.return语句可以出现在函数中的任何部分
# 2.函数可以没有return，此时函数并不返回值。
def fact_3(x,y=10):
    return x*y,x+y #同时可以将0个，1个或多个函数运算的结果返回给函数被调用处的变量

a,b = fact_3(99,2)
print(a,b)  #当函数使用return返回多个值，可以使用一个变量或多个变量保存结果。

#5.3变量的作用域，全局变量与局部变量
#5.3.1 局部变量
def multiply(x,y=10):
    z = x * y
    return z #z是函数内部使用的局部变量
s = multiply(99,2) #局部变量仅在函数内部有效，当函数退出时（此时，被调用结束）变量将不再存在
print(s)
# print(z) #会报错

#5.3.2 全局变量
n =2 #n为全局变量，即在函数之外定义的变量，其在程序执行全过程有效
def multiply1(x,y=10):
    global n #全局变量在函数内部使用时，需提前使用保留字global声明
    t = x*y*n
    return t
s1 = multiply1(99,2)
print(s1)

#对比一下两个例子，使用/不使用global
#1 使用global
m = 5
def fact2(x,y):
    global m #global保留字
    m = x*y  #m的值被修改
    a = m + 1
    return a
x1 = fact2(99,2)
print(x1) #199
print(m)  #198 由于在函数内使用了global保留字，m的值已被修改

#2 不使用global

m1 = 5
def fact3(x,y):
    m1 = x*y #没有使用global，m1此时为函数中局部变量
    a = m1 + 1
    return a
x2 = fact2(99,2) #调用结束，函数退出时，变量m1将不复存在
print(x2) #199
print(m1) #5 #所以m1的值还是最开始的5