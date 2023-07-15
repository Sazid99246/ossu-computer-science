name = input("Enter a file name: ")
fh = open(f"intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_09\{name}")
dict = {}
count = 0
for line in fh:
    if line.startswith("From:"):
        phrases = line.strip().split(" ")
        email = phrases[1]
        if email not in dict:
            dict[email] = 1
        else:
            dict[email] += 1

print(dict)
most_messages = None
max_value = 0
for email, count in dict.items():
    if count > max_value:
        most_messages = email
        max_value = count

if most_messages is not None:
    print(f"\n{most_messages} {str(max_value)}")
else:
    print("No messages found in the log.")