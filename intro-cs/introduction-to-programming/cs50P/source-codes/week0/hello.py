def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print(f"hello, ", to)

main()