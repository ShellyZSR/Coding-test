# .Split() function: breaks a string into parts and produces a list of strings
a = 'with three words'
b = a.split()
print(b) #['with', 'three', 'words']
print(len(b)) #3
print(b[0]) #with
# we can specify what delimiter character to use in spliting
#.split()是拿空格分割的，我们可以选择不同的划界符delimiter
x = 'first;second;third;four'
y = x.split(';') #记得加冒号
print(y)

#exercise 提取 outlook.com
email = 'From ShellyZSR@outlook.com Sat 19/17'
se = email.split()
z = se[1]
pieces = z.split('@')
print(pieces[1])

