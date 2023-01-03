try:
    hrs = int(input("Enter hours: "))
except:
    print('Error, please enter numeric input')
    quit()
try:
    rate = float(input("Enter rate: "))
except:
    print('Error, please enter numeric input')
    quit()

gpay = hrs * rate
print("Pay:", gpay)