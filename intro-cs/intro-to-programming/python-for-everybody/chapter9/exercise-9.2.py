file = open('assets/py4e/mbox-short.txt')
days = dict()
for line in file:
    words = line.split(" ")
    if len(words) < 3 or words[0] != "From":
        continue
    else:
        if words[2] not in days:
            days[words[2]] = 1
        else:
            days[words[2]] += 1
print(days)