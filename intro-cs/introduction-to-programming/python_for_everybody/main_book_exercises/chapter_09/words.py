word_dict = {}
file = open("words.txt")
for line in file:
    words = line.split(" ")
    for word in words:
        word_dict[word] = None
print(word_dict)