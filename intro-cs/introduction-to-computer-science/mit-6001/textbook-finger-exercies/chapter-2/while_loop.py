numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
count = 0
#concatenate X to toPrint numXs times
while count < numXs:
    toPrint += 'X'
    count += 1
print(toPrint)