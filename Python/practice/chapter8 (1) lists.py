# using index operator to look inside lists
friends = ['Shelly','Merry','Tony'] #(0,1,2)
print(friends[2])

#lists is mutable, we can change an element of a list using index operator
friends = ['Shelly','Merry','Tony']
friends[1] = 'Crystal'
print(friends) #['Shelly', 'Crystal', 'Tony']

number = [12,23,34,56]
number[3] = 45
print(number) #[12, 23, 34, 45]

# how long is a list: len(x)
number = [12,23,34,56]
print(len(number))

#Range function: range()
print(range(4))

friends = ['Shelly','Merry','Tony']
print(len(friends))
print(range(len(friends)))

# loop iteration
friends = ['Shelly','Merry','Tony']
for friend in friends:
    print('Happy New Year',friend)
#If we want to know where the variables are at the relative to the list.
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year',friend,i)

