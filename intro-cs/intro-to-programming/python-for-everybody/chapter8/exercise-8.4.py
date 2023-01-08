file = open("romeo.txt")
myList = []
for line in file:
    words = line.split()
    for word in words:
        if word in myList:
            continue
        myList.append(word)
print(sorted(myList))