s = input("Input: ")

for c in s:
    if c not in "AEIOUaeiou":
        print(c, end="")
print("")