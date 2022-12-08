#4.4 无限循环while
#1
n = 1
while n < 9:
    print(n)
    n = n+3
print("end")

#2 while-else，while循环正常执行之后，执行else语句
# (else语句中可放置判断循环执行情况的语句）
s = 'python'
num = 0
while num < len(s): #num0 Lens 2
    print(len(s),num)
    num +=1
    s = s[num:]
    #break

else:
    print('循环正常结束')
print('end')