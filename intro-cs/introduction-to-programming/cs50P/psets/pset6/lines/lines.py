import sys
import os.path

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif str(sys.argv[1]).endswith(".py") == False:
    sys.exit("Not a python file")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif os.path.exists(sys.argv[1]) == False:
    sys.exit("File does not exist")

else:
    with open(sys.argv[1], "r") as file:
        lines = file.read().splitlines()
        totalCount = len(lines)
        whitespace = 0
        comments = 0

        for line in lines:
            linecheck = line.rstrip().strip().split("\n")
            for x in linecheck:
                if len(x) < 1:
                    whitespace += 1
                elif len(x) > 0 and x.startswith('#'):
                    comments += 1

finalCount = totalCount - whitespace - comments
print(finalCount)