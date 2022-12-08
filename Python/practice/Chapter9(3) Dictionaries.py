# coutning pattern: counting words
counts = dict()
line = input('Enter a text:')

words = line.split()
print('words:',words)

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts:',counts)

# Definite loop (for loop) and dictionaries:
names = {'Shelly':1, 'Merry':2, 'Tony':3}

for key in names: #(这里循环的是Key，go through key rather than value)
    
    print(key, names[key])


#Retrieving lists of keys/values/both of them:
#1. print a list of keys
#(1)
jjj = {'Shelly':11, 'Merry':21, 'Tony':13}
print(list(jjj))
#['Shelly', 'Merry', 'Tony']

#(2)
jjj = {'Shelly':11, 'Merry':21, 'Tony':13}
print(jjj.keys())
#dict_keys(['Shelly', 'Merry', 'Tony'])

#2. print a list of values
jjj = {'Shelly':11, 'Merry':21, 'Tony':13}
print(jjj.values())
#dict_values([11, 21, 13])

#3 print a list of key-value pairs:
jjj = {'Shelly':11, 'Merry':21, 'Tony':13}
print(jjj.items())
dict_items([('Shelly', 11), ('Merry', 21), ('Tony', 13)])

# two iteration variables:
jjj = {'Shelly':11, 'Merry':21, 'Tony':13}
for k,v in jjj.items():
    print(k,v)