def main():
    first, operator, second = input().strip().split(" ")
    first = float(first)
    second = float(second)
    print(interpreter(first, operator, second))


def interpreter(first, operator, second):
    match operator:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second
        case "/":
            if second == 0:
                return "ZeroDivisionError"
            else:
                return first / second


main()
