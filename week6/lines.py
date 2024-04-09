import sys


def check_file():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguements")
    else:
        return sys.argv[1].endswith(".py")


def count_line():
    count = 0
    try:
        with open(sys.argv[1], "r") as file:
            for row in file:
                row = row.lstrip()
                if row != "" and (not row.startswith("#")):
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exit")
    else:
        return count


def main():
    if check_file():
        print(count_line())
    else:
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
