answer = str(input("Greeting: "))
answer = answer.lower().strip()
if answer.startswith("hello") == True:
    print("$0")
elif answer != "hello" and answer.startswith("h") == True:
    print("$20")
else:
    print("$100")