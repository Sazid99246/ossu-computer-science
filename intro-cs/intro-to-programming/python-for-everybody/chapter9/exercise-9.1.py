count = 0
file = open("assets/py4e/words.txt")
dictionary = dict()

for line in file:
    words = line.split(" ")
    for word in words:
        count += 1
        if word in dictionary:
            continue
        dictionary[word] = count

if "Python" in dictionary:
    print(True)
else:
    print(False)