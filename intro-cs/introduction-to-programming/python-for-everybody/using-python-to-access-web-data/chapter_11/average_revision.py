import re

filename = input("Enter file: ")
fhand = open(filename, 'r')

nums = []

for line in fhand:
    match = re.search("New\sRevision:\s(\d+)", line)
    if match:
        nums.append(int(match.group(1)))

print(sum(nums)/len(nums))