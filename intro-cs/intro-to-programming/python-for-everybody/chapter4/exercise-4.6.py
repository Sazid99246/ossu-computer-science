def computePay(tmp_hours, tmp_rate):
    if tmp_hours > 40:
        extraHours = tmp_hours - 40
        return (tmp_rate * 40) + (extraHours * tmp_rate * 1.5)
    else:
        return tmp_hours * tmp_rate

def check_for_float(input1):
    try:
        val = float(input1)                # Only allows input floats
        return val
    except ValueError:
        print('Error, please enter numeric input')
        quit()

input_hours = input("Enter Hours: ")
hours = check_for_float(input_hours)


input_rate = input("Enter Rate: ")
rate = check_for_float(input_rate)

pay = computePay(hours, rate)
print(pay)