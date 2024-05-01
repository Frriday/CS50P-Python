from validator_collection import checkers


def main():
    address = input("What's your email address? ")

    if checkers.is_email(address):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
