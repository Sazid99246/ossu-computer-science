# prompts user to answer to the question
text = str(input("What is the answer to the Great Question of Life, the Universe and Everything? "))

# converting the text to lower case, no space either side
answer = text.replace("-", " ").lower().strip()

# checking if the answer is valid or not
if answer == "forty two":
    print("Yes")
elif answer == "42":
    print("Yes")
else:
    print("No")