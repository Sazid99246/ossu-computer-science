file = open('mbox-short.txt')
for lx in file:
    ly = lx.rstrip()
    print(ly.upper())