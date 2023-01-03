try:
    number = float(input("Enter score: "))    
except ValueError:
    print('Bad score')
    quit()


if number > 0.0 and number < 0.6:
    print("F")
elif number >= 0.6 and number < 0.7:
    print("D")
elif number >= 0.7 and number < 0.8:
    print("C")
elif number >= 0.8 and number < 0.9:
    print("B")
elif number >= 0.9 and number < 1.0:
    print("A")
else:
    print("Bad Score")