import re

count = 0
file = open('assets/py4e/mbox-short.txt')
regex = input("Enter a regular expression: ")
regex_exp = str(regex)
for line in file:
    line = line.rstrip()
    if re.findall(regex_exp, line) != 0:
        count += 1
print(f"mbox.txt had {count} lines that matched {regex}")