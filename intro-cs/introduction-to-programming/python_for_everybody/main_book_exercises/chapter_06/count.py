def counter(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    print(count)

counter("banana", 'a')