try:
    hours = float(input("Enter hours: "))
except ValueError:
    print("Error, please enter numeric input")

try:
    rate_per_hour = float(input("Enter rate: "))
except ValueError:
    print("Error, please enter numeric input")
if hours < 40:
    gross_pay = hours * rate_per_hour
else:
    overtime = hours - 40
    gross_pay = rate_per_hour * 40 + overtime * rate_per_hour * 1.5
print("Pay: " + str(gross_pay))