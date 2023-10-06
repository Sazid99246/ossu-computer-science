def main():
    x = input()
    print(convert(x))

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()