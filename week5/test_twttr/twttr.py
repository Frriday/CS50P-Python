vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def main():
    msg = input("Input: ")
    print(shorten(msg))


def shorten(message):
    result = []
    for s in message:
        if s not in vowels:
            result.append(s)
    return "".join(result)


if __name__ == "__main__":
    main()
