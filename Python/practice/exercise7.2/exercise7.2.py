# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
count = 0
total = 0
#open and read the file
try:
    fhandle = open(fname,'r')
except:
    print('File can not be opened')
    quit()


for line in fhandle:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
#如果要从file line中提取数据，需要先在if循环中体现出来，用find和【】，最后在print
        x = line.find(':')
        spam = line[x+1:]
        spam = float(spam)
        total = total + spam
    # print(line)
    # print(count)

print('Average spam confidence:',total/count)

