name = input("Write your name: ")
index = len(name) - 1
while index >= 0:
    letter = name[index]
    print(letter)
    index -= 1
