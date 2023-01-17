################## Problem ##################
# Write a program that examines three variables—x, y, and z—and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.#

################## Solution ##################
x = int(input("Input x: "))
y = int(input("Input y: "))
z = int(input("Input z: "))

if x and y and z % 2 != 0:
    if x > y and x > z:
        print(x, "is the largest odd number")
    elif y > x and y > z:
        print(y, "is the largest odd number")
    else:
        print(z, "is the largest odd number")

elif x and y %2 != 0 and z %2 == 0:
    if x > y:
        print(x, "is the largest odd number")
    else:
        print(y, "is the largest odd number")

elif y and z %2 != 0 and x %2 == 0:
    if y > z:
        print(y, "is the largest odd number")
    else:
        print(z, "is the largest odd number")

elif x and z %2 != 0 and y %2 == 0:
    if z > x:
        print(z, "is the largest odd number")
    else:
        print(x, "is the largest odd number")
else:
    print("Sorry! There is no odd number")