#length of strings
fruit = 'apple'
print(len(fruit))

# Looping through strings 1(while)
fruit = 'apple'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# Looping through strings 2(for)
fruit = 'apple'
for letter in fruit:
    print(letter)

# Looping and Counting 字符串中某字母在某个单词中出现几次？
word = 'apple'
count = 0
for letter in word:
    if letter == 'p':
        count = count + 1
print('a =',count)

#slicing strings 从几到几中间是冒号！！！！！
x = 'Hello Shelly'
print(x[2:4])
print(x[ :5])
print(x[3: ])