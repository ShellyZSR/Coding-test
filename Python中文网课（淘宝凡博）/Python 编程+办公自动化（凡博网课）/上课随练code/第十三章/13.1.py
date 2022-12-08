#13 正则表达式 Regular expression (RE库）
#功能：实现对字符的一种过滤，解析字符串

#13.1 RE库匹配
#（1）re.match() 【从字符串的起始位置开始匹配，如果不是起始位置匹配成功的话，返回none】
#（2）re.search() 【不常用，有局限性】
#（3）re.findall()【搜索整个字符串，然后返回匹配正则表达式的所有内容】

import re
# message = '钟南山、李兰娟、王辰、张伯礼、陈薇、乔杰'
# result = re.match('李兰娟',message)
# print(result)  #返回：None

#13 正则表达式 （各类符号，详见Word）

'''任务1：从message中提取abcde中任意一个字母'''
# message = '11ndinwd123duenasfdncuio'
# result = re.search('[abcde]',message)
# print(result)
#<re.Match object; span=(3, 4), match='d'>
#re.search()匹配到第一个符合过滤条件的字符就会返回，不会再继续匹配

'''任务2：从message中找出字母+至少一个数字+字母：例如a7d;e77d'''
# message = '11ndinwd123duen2asfd6ncuio'
# result = re.search('[a-z][0-9]+[a-z]',message)
# print(result)

'''任务3：验证手机号码的正确性1开头的11位数字'''
# phone_num = input('请输入你的手机号码：')
# result = re.match('1[0-9]{10}',phone_num) #输了12位也能匹配到，有Bug
# print(result)
# result = re.findall('^1[0-9]{10}$',phone_num)
# print(result)

'''任务4：验证QQ号码的正确性,从5-11位数字，开头不能是0'''
QQ_num = input('请输入你的QQ号码：')
result = re.findall('^[1-9][0-9]{4,10}$',QQ_num)
print("你的QQ号是：", result)

