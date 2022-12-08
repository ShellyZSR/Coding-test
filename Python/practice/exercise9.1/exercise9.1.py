# 9.4 Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#  The program creates a Python dictionary 
# that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

# 文件中谁发的邮件次数最多
# 1. 读取文件
# 2. Built a list :name；Built a dictionary：counts
# 3. 逐行读取 > loop
#    4.split 建立List
#    5.提取the second word of those lines as the person [1]
#    6. 放进Name list中
#    7. 逐个读取名字 > loop
#        8. counts用get method，如果没有出现名字加进去，出现了+1（key:name; value: 出现的次数）

# 9. bigname = None; bigcounts = None
# 10. 逐个读取Dictionary里pairs of key and value  > loop
#     11. 如果 bigname = None or value > bigcounts, remember
#         else: continue
# 12. print()
#%%
fhandle = open('mbox-short.txt', 'r')
names = list()
counts = dict()

#%%
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From'):
        sp = line.split()
        if len(sp) > 2:
            email = sp[1]
            names.append(email)
print(names)

for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)

bigname = None
bigcounts = None
for name,count in counts.items():
    if bigcounts is None or count > bigcounts:
        bigname = name
        bigcounts = count
print(bigname,bigcounts)
        


