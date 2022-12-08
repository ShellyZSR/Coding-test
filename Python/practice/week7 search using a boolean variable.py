found = False
print("Before", found)
for number in [2,3,4,5,6,7,8,9,67,85]:
    if number == 3:
        found = True
    print(found,number)
print("Finish",found)