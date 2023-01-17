''' Problem
Replace the comment in the following code with a while loop.
numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
print(toPrint)
'''

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
itersLeft=numXs
while itersLeft != 0:
    toPrint += 'X'
    itersLeft -= 1
print(toPrint)