file = open("romeo.txt")
words = []
while True:
    line = file.readline()
    if not line:
        break
    w = line.split("\n")
    print(w)
    w = w[0]
    w = w.split(" ")
    for i in range(len(w)):
        string = w[i]
        if string not in words:
            words.append(string)
words.sort()
# print(words)
file.close()
