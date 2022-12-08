#二、random库：使用random库主要目的是生成随机数。
import random
#1。random.random():生成一个[0.0, 1.0)之间的随机小数(包含0，不包含1）
# a = random.random()
# print(a)

#2. random.seed(a=None):初始化随机数种子，默认值为当前系统时间
# random.seed(1) #此句代码，把随机值固定
# a = random.random()
# print(a)#无论Run几次，都会是同一个小数，只要seed()括号里参数相同

#3。random.randint(a, b):生成一个[a,b]之间的整数 (开区间）
# print(random.randint(1,5))

#4. random.randrange(start, stop[, step]):生成一个[start, stop)之间以step为步数的随机整
# print(random.randrange(1,10)) #生成1-10之间一个随机整数
# print(random.randrange(1,10,2)) #生成1-10之间步长为2的一个随机整数 【1，3，5，7，9】

#5. random.uniform(a, b): 生成一个[a, b]之间的随机小数
# print(random.uniform(1,4))

#6. random.choice(seq):从序列类型(例如：列表)中随机返回一个元素
# a = ['石头','剪刀','布']
# print(random.choice(a))

#7. random.shuffle(seq):将序列类型中元素随机排列，返回打乱后的序列
# a = ['石头','剪刀','布']
# random.shuffle(a) #打乱a顺序
# print(a)

#8. random.sample(pop, k):从pop类型中随机选取k个元素，以列表类型返回 (没有规定pop必须是什么类型）
# a = ['石头','剪刀','布']
# b = ('石头','剪刀','布')
# print(random.sample(a,2))
# print(random.sample(b,2))
# # ['布', '剪刀']
# # ['布', '剪刀']

#9. random实例：石头剪刀布游戏
a = ['石头','剪刀','布']
b = input('请在"石头""剪刀""布"中作出选择!你的选择是:',)
print("你的选择是：",b)
bot = random.choice(a)
print('电脑的选择是：',bot)
if bot =='石头' and b == '石头':
    print("平局")
if bot =='石头'and b == '剪刀':
    print("你输啦！")
if bot =='石头'and b == '布':
    print("你赢啦！")

if bot =='剪刀'and b == '石头':
    print("你赢啦！")
if bot =='剪刀'and b == '剪刀':
    print("平局")
if bot =='剪刀'and b == '布':
    print("你输啦！")

if bot =='布'and b == '石头':
    print("你输啦！")
if bot =='布'and b == '剪刀':
    print("你赢啦！")
if bot =='布'and b == '布':
    print("平局！")