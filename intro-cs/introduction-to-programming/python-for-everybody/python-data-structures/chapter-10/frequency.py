import string

counts = 0                          # Initialize variables
dictionary_counts = dict()
relative_lst = list()

fname = input('Enter file name: ')
try:
    fhand = open(f"intro-cs\introduction-to-programming\python_for_everybody\main_book_exercises\chapter_09\{fname}")
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    # Removes numbers and punctuation then sets all letters to lower case
    words = line.split()
    for word in words:
        for letter in word:
            # Count each letter for relative frequencies
            counts += 1
            if letter not in dictionary_counts:
                dictionary_counts[letter] = 1
            else:
                dictionary_counts[letter] += 1

for key, val in list(dictionary_counts.items()):
    relative_lst.append((val / counts, key))  # Computes the relative frequency

relative_lst.sort(reverse=True)         # Sorts from highest rel freq

for key, val in relative_lst:
    print(key, val)