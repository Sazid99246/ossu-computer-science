import re
file = open('assets/py4e/regex_num.txt')

newlist = list()
for line in file :
    line = re.findall('[0-9]+', line)
    for number in line :
        newlist.append(int(number)) # creates newlist with int line values
print(sum(newlist))
