#3.9 对字符串的操作
name = "python是最接近人工" + "智能的语言!"
print(name * 3)
# 输出为：python是最接近人工智能的语言!python是最接近人工智能的语言!python是最接近人工智能的语言!

print("语言" in name)
# True
print("bushi语言" in name)
# False


#对字符串处理的内置函数
#1
a = len("python是最接近人工智能的语言!")
print(a)
#2
b = 10 + 10j
print(type(b))
# 输出：<class 'complex'>
b = str(b)
print(b,type(b))
#输出：(10+10j) <class 'str'>

#3 chr()返回Unicode编码x对应的单字符
#4 ord()返回单字符x表示的Unicode编码
c = chr(89)
print(c, type(c))
#输出：Y <class 'str'>
d = ord("Y")
print(d)
#输出：89

#5 hex(x)返回整数x对应十六进制数的小写形式字符串
print(hex(26))
#输出：0x1a

#6 oct(x)返回整数x对应八进制数的小写形式字符串
print(oct(26))
#输出:0o32