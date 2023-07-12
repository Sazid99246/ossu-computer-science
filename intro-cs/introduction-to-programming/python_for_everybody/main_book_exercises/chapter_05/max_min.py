num = 0
total = 0
num_list = []

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
        num_list.append(fval)
    except:
        print("Invalid input")
        continue

    num = num + 1
    total = total + fval

        
lowest = min(num_list)
highest = max(num_list)
print({
    "total": total,
    "length": num,
    "maximum": highest,
    "minimum": lowest
})
