file = input('Enter a file name: ')
fhand = open(f'intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_08\{file}')
emails = []
for line in fhand:
    if line.startswith("From"):
        words = line.split(" ")
        mail = words[1]
        emails.append(mail)

for email in emails:
    print(email.strip())
print(f"There were {str(len(emails))} lines in the file with From as the first word")