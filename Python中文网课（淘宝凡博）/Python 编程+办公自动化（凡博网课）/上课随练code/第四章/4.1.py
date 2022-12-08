# 4.1 判断条件及组合

a = 4
b = 5
print(a<b,a<=b,a>b,a>=b,a!=b)
#True True False False True


#Python语言使用保留字 and not 和 or 对条件进行逻辑运算或组合
print(a > 6 or (a<5 and a < 8))

#补充：比较两个字符串的大小：依次比较每个字符串中字符对应的Unicode的值
print(ord('中'),ord('国'),'中'> "国")
print('python'>"Python")