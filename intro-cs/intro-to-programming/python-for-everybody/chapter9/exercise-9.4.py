file = open('assets/py4e/mbox-short.txt')
mail = dict()
maximum = 0
maximum_address = ''

for line in file:
    words = line.split(" ")
    if words[0] != "From":
        continue
    else:
        if words[1] not in mail:
            mail[words[1]] = 1
        else:
            mail[words[1]] += 1

for address in mail:
    if mail[address] > maximum:
        maximum = mail[address]
        maximum_address = address

print(maximum_address, maximum)