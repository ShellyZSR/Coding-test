#4.5 异常处理try-except

try:
    n = eval(input("请输入一个数字："))
    print("该数字的3次方为：", n**3)
except:
    print("请重新输入一个数字")