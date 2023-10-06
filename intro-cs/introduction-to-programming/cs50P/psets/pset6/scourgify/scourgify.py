import sys
import csv

def main():
    check_argv()
    student = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                student.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})

        with open(sys.argv[2], "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for row in student:
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def check_argv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a csv file")

if __name__ == "__main__":
    main()