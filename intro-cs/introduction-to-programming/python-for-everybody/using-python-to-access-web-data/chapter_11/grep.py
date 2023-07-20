import re

counter = 0
file = 'mbox.txt'
fhand = open(file)
input_regex = input("Enter a regular expression: ")
for line in fhand:
    line = line.rstrip()
    if re.findall(input_regex, line):
        counter += 1
print(file + f' had {str(counter)} lines that matched {input_regex}')