# 函数pow(x,y):用来计算x的y次方的值
a = 7
b = 11
print(pow(a,b))

#函数round():用来解决不确定尾数的问题
# round(x,d):表示对x进行四舍五入，其中参数d为指定保留的小数位数，即保留小数点后第d位小数

a = round(0.1+0.2, 1) #对0.1+0.2四舍五入，保留小数点后第1位小数
b = round(1.2346, 2) #对1.2346四舍五入，保留小数点后第2位小数
c = round(1.2346, 3)
print(a)
print(b)
print(c)
#输出结果为：
#0.3
#1.23
#1.235