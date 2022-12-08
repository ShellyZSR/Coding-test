# eval()函数，能够以Python表达式的方式，解析并执行字符串，将返回结果输出
# 可以理解为，eval('1.2 + 3.4'), eval可以将''去除掉,将引号里的内容当作一个表达式来进行运算
# eval()经常与input()函数一起使用，用来直接捕获用户输入的数字
a = eval(input('请输入数字：'))
value = a * 3 + 5
print(value,type(value))
# 如果用户输入的不是数字的话,python将会报错，
# 因此eval()还有一个好的功能就是：要求用户必须输入数字

a1 = input("请输入数字：") #input输入进来的是string
value1= eval(a1) + 5 + 6 #eval()函数之后，返回为integer了
print(a1,type(a1))
print(value1,type(value1))
# 输入134，输出为
# 134 <class 'str'>
# 145 <class 'int'>