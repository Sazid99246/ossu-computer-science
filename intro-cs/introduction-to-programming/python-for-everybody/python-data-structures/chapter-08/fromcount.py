fname = input('Enter a file name: ')
fh = open(f'intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_08\{fname}')
mails = []
count = 0
for line in fh:
    if line.startswith("From:"):
        words = line.split(" ")
        mail = words[1].strip()    
        print(mail)
        count += 1

print("There were", str(count), "lines in the file with From as the first word")