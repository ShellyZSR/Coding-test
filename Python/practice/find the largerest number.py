larger_so_far = -1
print("Before",larger_so_far)
for number in [23,3,25,14,35,24,36,57,46]:
    if number > larger_so_far:
        larger_so_far = number
    print(larger_so_far, number)
print("Finish",larger_so_far)