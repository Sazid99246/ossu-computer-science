import re
with open('regex_sum_1844691.txt') as file:
    content = file.read()
numbers = re.findall('\d+', content)
total = 0
for num in numbers:
    total += int(num)
print(total)