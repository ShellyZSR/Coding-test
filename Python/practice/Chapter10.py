#Tuples are like lists (跟list一样的地方)
x = ('Shelly', 'Merry', 'Tony')
print(x)
y = (1,23,45)
print(max(y))

for number in y:
    print(number)

# tuples are not mutable
# z = (1,21,23)
# z[2] = 24
# Traceback (most recent call last):
#   File "/Users/teresa624/Documents/Coding/Python/practice/Chapter10.py", line 12, in <module>
#     z[2] = 24
# TypeError: 'tuple' object does not support item assignment
# 192:practice teresa624$ 

#Tuples and assignment:
(c,d) = (4, 'fred')
print(c)
print(d)

#tuples and dictionaries: .items() method in dictionary returns a list of tuples
dictionary = dict()
dictionary['Shelly'] = 2
dictionary['Merry'] = 4
for k,y in dictionary.items():
    print(k,y)
#(Shelly 2  Merry 4)   

#tuples are comparable;
print((0,1,2) > (0,1,1))
print(('apple','pear','salad') > ('apple','pear', 'sandwich'))
# True
# False

#Sorting lists of tuples:
d = {'a':10, 'c':6, 'b':9}
print(d.items())
print(sorted(d.items()))

#using sorted
#sorted by key
dd = {'a':10, 'c':41, 'b':9}
for k,v in sorted(dd.items()):
    print(k,v)


dd = {'a':10, 'c':41, 'b':9}
x = list()
print(dd.items())

#循环dd tuples里面的每一组数据，并把value 和 key的位置调换，然后加进 x list中
for k,v in dd.items():
    x.append((v,k))
print(x)

#按照Value从小到大的顺序，Sort x
x = sorted(x)
print(x)

#按照Value从大到小的顺序，Sort x
x = sorted(x, reverse=True)
print(x)