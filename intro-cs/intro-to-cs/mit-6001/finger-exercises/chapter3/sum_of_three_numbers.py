s = "1.23, 2.4, 3.123"
sum = 0
nums = s.split(",")
for num in nums:
    sum += float(num)
print(sum)