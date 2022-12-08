# 3.10 数字类型的转换
x = "3"
x = int(x)
print(x, type(x))
# 3 <class 'int'>

y = 3.14
y = int(y)
print(y, type(y))
# 3 <class 'int'>
# int('3.14')不可🙅，会报错

z = 3
z = float(z)
print(z, type(z))
# 3.0 <class 'float'>

a = 3234
a = str(a)
print(a,type(a))
# 3234 <class 'str'>
