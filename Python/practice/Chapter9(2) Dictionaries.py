# exercise count names:
counts = dict()
names = ['cesv', 'cwen', 'csev', 'zqian', 'csev']
for name in names:
    if not name in counts:
        counts[name] = 1

    else:
        counts[name] = counts[name] + 1
print(counts)

# a easier way to do the above thing: using get method ---- dictionary.get(key,default value)
counts = dict()
names = ['cesv', 'cwen', 'csev', 'zqian', 'csev']
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)


