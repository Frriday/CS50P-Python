import sys
import csv
from tabulate import tabulate


def check_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguements")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    else:
        return sys.argv[1].endswith(".csv")


def print_table():
    menu = []
    if check_file():
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
                    menu.append(row)
        except FileNotFoundError:
            sys.exit("File does not exit")
        else:
            print(tabulate(menu, tablefmt="grid", headers="keys"))
    else:
        sys.exit("Not a CSV file")


def main():
    print_table()


if __name__ == "__main__":
    main()
