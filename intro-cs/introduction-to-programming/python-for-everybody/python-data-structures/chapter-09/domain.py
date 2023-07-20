file = input("Enter a file name: ")
fh = open(f"intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_09\{file}")
dict = {}
count = 0
for line in fh:
    if line.startswith("From:"):
        phrases = line.strip().split(" ")
        email = phrases[1]
        email_letters = email.split()
        icon_index = email.index('@')
        domain_with_icon = email[icon_index:]
        domain = domain_with_icon.replace("@", "")
        if domain not in dict:
            dict[domain] = 1
        else:
            dict[domain] += 1

print(dict)