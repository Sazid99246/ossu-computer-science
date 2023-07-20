file = input('Enter a file name: ')
tot = 0
lines = 0
fhand = open(f'intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_07\{file}')
for line in fhand:
    if line.startswith("X-DSPAM-Confidence: "):
        lines += 1
        floatStr = float(line[19:])
        tot += floatStr

avg = tot / lines
print(f"Average spam confidence: {str(avg)}")