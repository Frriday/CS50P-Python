import re


def count(s):
    return len(re.findall(r"\bum\b", s, flags=re.IGNORECASE))


def main():
    print(count(input("Text: ")))


if __name__ == "__main__":
    main()
