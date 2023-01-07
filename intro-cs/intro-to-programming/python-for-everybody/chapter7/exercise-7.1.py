file = open('./file.txt')
for lx in file:
    ly = lx.rstrip()
    print(ly.upper())