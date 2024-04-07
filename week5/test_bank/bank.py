def main():
    greet = input()
    print(f"${value(greet)}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100
