def computgrade(number):
    if number > 0.0 and number < 0.6:
        return "F"
    elif number >= 0.6 and number < 0.7:
        return "D"
    elif number >= 0.7 and number < 0.8:
        return "C"
    elif number >= 0.8 and number < 0.9:
        return "B"
    elif number >= 0.9 and number < 1.0:
        return "A"
    else:
        return "Bad Score"

input_score = input("Enter Score")
score = 0.0

try:
    score = float("Enter score: ")   
except ValueError:
    print('Bad score')
    quit()

grade = computgrade(score)
print(grade)