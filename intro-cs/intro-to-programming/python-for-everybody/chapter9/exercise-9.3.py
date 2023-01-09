file = open('assets/py4e/mbox-short.txt')
mail = dict()
for line in file:
    words = line.split(" ")
    if words[0] != "From":
        continue
    else:
        if words[1] not in mail:
            mail[words[1]] = 1
        else:
            mail[words[1]] += 1
print(mail)