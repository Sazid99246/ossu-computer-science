'''
Problem
Write a program that asks the user to input 10 integers, and then
prints the largest odd number that was entered. If no odd number was entered, it
should print a message to that effect.
'''
largestNum = 0
itersLeft = 10

while itersLeft != 0:
    num = int(input("Please enter an integer: "))
    itersLeft -= 1
    if num%2 != 0 and num > largestNum: #compare only if number is odd
        largestNum = num
    
if largestNum == 0:
    print("No odd number entered")
else:
    print("Largest odd number is " + str(largestNum) + ".")