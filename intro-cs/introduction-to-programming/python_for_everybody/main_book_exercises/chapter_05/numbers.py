num = 0
total = 0

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue

    num = num + 1
    total = total + fval

print(total, num, total/num)