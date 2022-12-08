
smallest = None
print("Before")
for number in [13,23,2,3,56,46,34,67,45,33]:
    if smallest is None: #意味着：如果smallest是空的话，（表示开始程序）
        smallest = number
    elif number < smallest:
        smallest = number
    print(smallest,number)
print("Finish",smallest)