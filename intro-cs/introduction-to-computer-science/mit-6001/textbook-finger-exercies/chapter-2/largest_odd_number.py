'''
Write a program that examines three variables—x, y, and z—and
prints the largest odd number among them. If none of them are odd, it should
print a message to that effect
'''

odd_numbers = []

def is_odd(a):
    return a % 2 != 0
        
def finding_largest_odd(x, y, z):
    nums = [x, y, z]
    if is_odd(x) == False and is_odd(y) == False and is_odd(z) == False:
        print("Sorry, none of the numbers is odd!")
    else:
        for num in nums:
            if is_odd(num):
                odd_numbers.append(num)
        print(str(max(odd_numbers)) + " is the largest odd number among the three numbers")

finding_largest_odd(3, 9, 5)