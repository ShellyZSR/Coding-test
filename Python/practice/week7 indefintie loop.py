#indefinite loop一直循环 until some conditions are false or break

n = 5
while n > 0:
    print(n)
    n = n-1
print("Finish")
print(n)

#zero-trip loop
n = 0
while n > 0:   #False
    print("larger") #never run
print("dry off")

#break statement
while True: #infinite loop表示一直为真
    x = input(">")
    if x == "done":
        break #it jumps out of the loop
    print(x)
print("Finish")

#continue statement 结束当前循环，重新开始循环
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("finish")

