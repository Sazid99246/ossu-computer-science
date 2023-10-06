text = input("Expression: ")

x, y, z = text.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print(f"{x + z}")
elif y == "-":
    print(f"{x - z}")
elif y == "*":
    print(f"{x * z}")
elif y == "/":
    print(f"{x / z}")