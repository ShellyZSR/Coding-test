# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list 
# and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

fhandle = open('romeo.txt','r')
x = list()

for line in fhandle:
    line = line.rstrip()
    sline = line.split()
    
    for word in sline:
        if word in x:
            continue
        x.append(word)
print(x)

# 1. 不要空想，想到了就变成代码打出来
# 2. 不知道是啥就print一下
# 3. 看不懂的语法直接复制到baidu查就行
# 4. 逻辑关系一定要事先理清
# 5. 纸上谈来终觉浅，绝知此事要coding！

    

    
    
    