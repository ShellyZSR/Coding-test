# counting
count = 0
print('before',count)
for number in [9,41,53,67,90]:
    count = count + 1
    print(count,number)
print('Finish, total:',count)


# total
total = 0
print("Before",total)
for number in [2,3,5,29,40,34,23,33,45]:
    total = total + number
    print(total,number)
print("After, Total:",total)

# Average
count = 0
total = 0
print("Before",count)
for value in [1,23,34,45,67,88]:
    count = count + 1
    total = total + value
    print(count,total,value)
print("After", count,total,total/count)