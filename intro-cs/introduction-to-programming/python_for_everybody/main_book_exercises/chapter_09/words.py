word_dict = {}
file = open("intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_09\words.txt")
for line in file:
    words = line.split(" ")
    for word in words:
        word_dict[word] = None
print(word_dict)