file = open("assets/py4e/mbox-short.txt")
line_count = 0
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    line_count += 1
print(f'There were {line_count} lines in the file with From as the first word')