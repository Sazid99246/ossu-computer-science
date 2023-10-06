import sys
import inflect
p = inflect.engine()

namesList = []

while True:
    try:
        names = input("Name: ").title()
        if len(names) < 1:
            sys.exit()

        namesList.append(names)
        output = p.join(namesList)

    except EOFError:
        print('\n')
        print("Adieu, adieu, to " + output)
        break
    else:
        continue