#3.10 字符串的处理方法
a = ".....Python is an Excellent Language.#"
print(a)

#1 a.lower()返回字符串a的副本，全部字符小写
print(a.lower())
#2 a.upper()返回字符串a的副本，全部字符大写
print(a.upper())
#3
print(a.split('e'))
print(a.split())
#4
print(a.count('e'))
#5
print(a.replace("e","P"))
#6
print(a.center(50,"2"))
#7
print(a.strip('.#'))
print(a.strip("."))
#8
print(a.join('@@@'))