def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        for i in range(len(s)):
            if s[i].isnumeric():
                s = s[i : len(s)]
                s2 = s[0 : i]
                return not s.startswith("0") and s.isdecimal() and (len(s2) >= 2)
    else:
        return False

    return True

main()
