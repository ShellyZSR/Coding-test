print("Before")
count = 0
for number in [1,23,34,56,45,67,78,39,549]:
    if number > 50:
        count = count + 1
        print("Larger than 50",number)
print("Finish", count)