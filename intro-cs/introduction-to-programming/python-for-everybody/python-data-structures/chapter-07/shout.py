file = input('Enter a file name: ')
fhand = open(f'intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_07\{file}')
for line in fhand:
    print(line.upper().strip())