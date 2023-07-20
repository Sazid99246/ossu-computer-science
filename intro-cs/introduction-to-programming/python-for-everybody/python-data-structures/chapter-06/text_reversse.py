def reverse(str):
    index = len(str) - 1

    while index >= 0:
        print(str[index])
        index -= 1

reverse("I am Sazid.")