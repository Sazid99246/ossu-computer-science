import csv
import sys
from tabulate import tabulate
from io import StringIO

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if str(sys.argv[1]).endswith(".csv") == False:
    sys.exit("Not a csv file")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

else:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file, delimiter=',')
        headers = next(reader)

        tables = []
        for row in reader:
            tables.append(row)

        print(tabulate(tables, headers, tablefmt="grid"))
