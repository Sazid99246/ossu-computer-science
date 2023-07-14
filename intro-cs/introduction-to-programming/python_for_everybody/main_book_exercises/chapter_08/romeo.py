file = input("Enter file: ")
fhand = open(f'intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_08\{file}')
new_arr = []
for line in fhand:
    words = line.split(" ")
    for word in words:
        if word not in new_arr:
            new_arr.append(word)
        else:
            break
new_arr.sort()
print(new_arr)
