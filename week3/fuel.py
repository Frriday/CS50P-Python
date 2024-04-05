while True:
    fraction = input("Fraction: ")
    try:
        #在这里对字符串进行分割是必要的，这样可以处理在输入时为输入“/”
        #的情况，直接抛出一个ValueError在下面统一捕捉处理
        first, second = fraction.split("/")
        first = int(first)
        second = int(second)
        if first > second:
            raise ValueError
        result = round(first / second, 2)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        result = int(result * 100)
        if result <= 1:
            print("E")
        elif result >= 99:
            print("F")
        else:
            print(f"{result}%")
        break
