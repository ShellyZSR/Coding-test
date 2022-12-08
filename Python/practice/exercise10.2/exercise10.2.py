# #10.2 Write a program to read through the mbox-short.txt 
# and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time 
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, 
# print out the counts, sorted by hour as shown below.

# 邮件发送时间的分布
# 1. 打开文件
# 2. 逐行读取> loop
#     3.把每行右侧的分界符去掉
#     4.如果If由From开始，把这行提取出来
#         5.Split每行，提取时间
#         6.再Split（冒号），提取小时Hour
#         7.Hour放进dictionary中，逐个读取Hour
#             8.统计数量用Get method
#             9. items，并排序


fhandle = open('mbox-short.txt', 'r')
hours = list()
d = dict()
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        time = time.split(':')
        hours.append(time[0])
print(hours)

for hour in hours:
    d[hour] = d.get(hour,0) + 1
print(d)

for key,value in sorted(d.items()):
    print(key,value)
    
