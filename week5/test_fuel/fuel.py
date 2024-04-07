#注意：在本题中我们不应该捕获任何异常，否则在测试时会出现为未抛出一场的问题，导致无法通过
def main():
    percent = convert(input("Fraction: "))
    print(gauge(percent))


def convert(fraction):
    first_num, second_num = fraction.split("/")

    first_num = int(first_num)
    second_num = int(second_num)
    if second_num == 0:
        raise ZeroDivisionError
    if first_num > second_num:
        raise ValueError
    percent = first_num / second_num

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
