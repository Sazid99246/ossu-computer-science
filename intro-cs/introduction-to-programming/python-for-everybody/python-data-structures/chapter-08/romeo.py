file = input("Enter file: ")
fhand = open(f'intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_08\{file}')
new_arr = []
for line in fhand:
    lst = []
    for line in fhand:
        word_list = line.split()
        for word in word_list:
            if word not in lst:
                lst.append(word)
lst.sort()
print(lst)
