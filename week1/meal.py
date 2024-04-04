def main():
    time = input("Enter now time ").strip()
    time = convert(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    return float(time.replace(":", "."))


if __name__ == "__main__":
    main()
