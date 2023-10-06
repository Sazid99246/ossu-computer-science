def main():
    x = int(input("What's x: "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()