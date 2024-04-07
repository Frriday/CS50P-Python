def main():
    percent = convert(input("Fraction: "))
    print(gauge(percent))


def convert(fraction):
    while True:
        first_num, second_num = fraction.split("/")
        try:
            first_num = int(first_num)
            second_num = int(second_num)
            if second_num == 0:
                raise ZeroDivisionError
            if first_num > second_num:
                raise ValueError
            percent = first_num / second_num
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return round(percent, 2) * 100


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"

if __name__ == "__main__":
    main()
