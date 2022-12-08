#From Shelly k19009936@kcl.ac.uk to Jane
data = 'From Shellly k19009936@kcl.ac.uk to Jane'
x = data.find('@')
print(x)
y = data.find(' ',x)
print(y)
host = data[x+1 : y]
print(host)
