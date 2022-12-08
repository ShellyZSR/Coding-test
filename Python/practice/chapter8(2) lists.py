# Comcatenating lists:
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# Slicing lists using ':'
x = [12,45,36,78,79]
print(x[1:3]) #(up to but not including 3)
# [45,36]
print(x[:4])
#[12, 45, 36, 78]
print(x[:])
#[12, 45, 36, 78, 79]

#Methods for lists
#1: .append() :building a list
fruit = list()
fruit.append('apple')
fruit.append('pear')
fruit.append(4)
print(fruit)

#2 Is someting in a list? Using in/not in
some = [1,23,45,25,10]
print(23 in some)
print(22 in some)
print(22 not in some)
# True
# False
# True

#3 .sort(): let lists sort themselves
family = ['Shelly','Merry','Tony']
family.sort()
print(family) #['Merry', 'Shelly', 'Tony']
print(family[1]) #Shelly


#Built-in functions and lists
number = [12,23,34,45,56,67,47]
print(len(number))
print(max(number))
print(min(number))
print(sum(number))
print(sum(number)/len(number))

#exercise:
total = 0 
count = 0
while True:
    inp = input('Enter a number')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1

average = total/count
print('count:',count)
print('total:',total)
print(average)

#和下面这种用List的方法一致，唯一不同是第二种更占内存
valuelist = list()
while True:
    inp = input('Enter a number')
    if inp == 'done': break
    value = float(inp)
    valuelist.append(value)

print(len(valuelist))
print(sum(valuelist))
print(sum(valuelist)/len(valuelist))