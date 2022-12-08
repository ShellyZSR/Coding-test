#4.2
#1. 单分支结构： if 语句

#判断用户输入整数的奇偶性
a = eval(input('请输入你心中所想的一个整数：'))
if a % 2 == 1:
    print('没错！你脑海里的数字是一个奇数')
print("你输入的数字是：", a)
print('end')

#判断用户输入数据的特性（结合and 和 or 的知识点）
b = eval(input('请输入你心中所想的一个整数：'))
if b % 3 == 0 or b%5 == 0:
    print('哇！你脑海里的数字是：', b, '它能被3整除，或能被5整除')
# if b % 3 == 0 and b % 5 == 0:
    # print('哇！你脑海里的数字是：',b, '它即能被3整除，也能被5整除')

print("你输入的数字是：", b)
print('end')

##注意：Python语言中，任何非零的数值、非空的数据类型都等价于True，0等价于False，可以直接用作判断条件。
a1 = eval(input('请输入你心中所想的一个整数：')) #17 ##22
if a1 % 2 : #17%2=1(等价于True）##22%2=0(等价于False)
    print('没错！你脑海里的数字是一个奇数')
print("你输入的数字是：", a1)
print('end')

#4.2
#2. 二分支结构： if-else 语句

#判断用户输入整数的特性
a = eval(input('请输入你心中所想的一个整数：'))
if a % 3 == 0 and a % 5 == 0:
    print(a,"输入数字即能整除3，也能整除5")
else:
    print(a,"不能同时被3和5整除")
print('end')a

#二分支结构简洁的表达方式
#格式： 表达式 if 条件else 表达式2
s = eval(input('请输入你心中所想的一个整数：'))
token = "可以" if s % 3 == 0 and s % 5 == 0 else "不可以"
print("输入的数字{}同时被3和5整除".format(token))

#3. 多分支结构： if-elif-else 语句

#百分制成绩转化为五分制成绩（五个等级ABCDE）
score = eval(input('请输入您的百分制成绩:'))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print("你的成绩的五分制等级为：{}".format(grade))