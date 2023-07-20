file = input('Enter a file name: ')
try:
    if file == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    fhand = open(f'intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_07\{file}')
except FileNotFoundError:
    print("File cannot be opened:", file)
    exit()

lines = 0
for line in fhand:
    if line.startswith("Subject:"):
        lines += 1
print(f"There were {str(lines)} subject lines in {file}")