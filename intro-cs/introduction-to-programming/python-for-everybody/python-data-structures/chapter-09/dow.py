file = input("Enter a file name: ")
fh = open(f"intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_09\{file}")
dict = {}
count = 0
for line in fh:
    if line.startswith("From"):
        phrases = line.split(" ")
        if len(phrases) > 2:
            day = phrases[2]
            if day not in dict:
                dict[day] = 1
            else:
                dict[day] += 1

print(dict)