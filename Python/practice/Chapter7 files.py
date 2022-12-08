#the newline character
x = 'Hello\nWorld'
print(x)
# \n is one character
stuff = 'x\ny'
print(len(stuff))# lenth = 3 x \n y 

#Counting lines in a file
fhand = open('filename','r')
count = 0
for line in fhand:
    count = 0 + 1
print('Line Count:',count)

#reading the whole file
# .read()

#searching through a file
fhand = open('filename')
for line in fhand:
    if line.startswith('From:'):
        print(line)
# using .rstrip() to strip newlines
fhand = open('filename')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
#skipping with continue (跟上面的代码实现的功能/跑出来的东西是一样的，只是逻辑是反的)
fhand = open('filename')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'): #(会Skip那些不是以From开头的line)
        continue
print(line)

#using in to select lines:
fhand = open('filename')
for line in fhand:
    line = line.rstrip()
    if not ‘something' in line:
        continue
print(line)

#prompt for file name:
fname = input('File name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There were',count, 'Subject lines in', fname)
# if user types a bad file name, how to compensate?
# using try/except + quit()
fname = input('File name: ')
try:
    fhand = open(fname)
except:
    print("File name can not be opened:",fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There were',count, 'Subject lines in', fname)