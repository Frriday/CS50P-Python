import csv
import sys



def check_arguements():
    if len(sys.argv) == 3:
        return sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguements")
    else:
        sys.exit("Too many arguements")


def convert():
    list = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name, first_name = row["name"].split(",")
                list.append({"first": first_name.strip(),
                             "last": last_name.strip(),
                             "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File does not exit")
    else:
        return list


def main():
    if check_arguements():
        with open(sys.argv[2], "w") as file:
             writer = csv.DictWriter(file, ["first", "last", "house"])
             writer.writeheader()
             for msg in convert():
                writer.writerow(msg)
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
