hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40:
    extraHours = hours - 40
    pay = (rate * 40) + (extraHours * rate * 1.5)
else:
    pay = hours * rate
print(pay)