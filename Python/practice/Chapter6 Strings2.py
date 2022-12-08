# String Concatenation
a = 'Hello'
b = a + " " + 'Shelly'
c = a + 'Merry'
print(b)
print(c)
#(if you need a space between two strings, you should concatenate a space" ")

#using in as a logical operator
fruit = 'apple'
print('a' in fruit)
print('b' in fruit)
if 'a' in fruit:
    print('Got it!')

#Strings comparison
word = input()
if word == 'banana':
    print('all right, bananas')
elif word > 'banana':
    print("Your word," + word + ",comes after banana")
else:
    print("Your word," + word + ",comes before banana")

#String library
#1 .lower() give back a lowercase copy
x = 'Hello Shelly'
y = x.lower()
print(y)
z = 'HELLO MERRY'
print(z.lower())
print('Hello Yo'.lower())