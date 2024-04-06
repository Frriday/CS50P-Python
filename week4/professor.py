import random
vaild_level = [1, 2, 3]

def main():
    score = 0
    level = get_level()
    for _ in range(10):
        first_num = generate_integer(level)
        second_num = generate_integer(level)
        count = 0
        while True:
            try:
                count += 1
                result = int(input(f"{first_num} + {second_num} = "))
                if result != (first_num + second_num):
                    raise ValueError

            except ValueError:
                print("EEE")
                if count >= 3:
                    print(f"{first_num} + {second_num} = {first_num + second_num}")
                    break
            else:
                score += 1
                break
    print(f"Score: {score}")

def get_level():
    level = 0
    while True:
        try:
            level = int(input("Level: "))
            if level not in vaild_level:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    return random.randint(10**(level - 1), 10**level - 1)


if __name__ == "__main__":
    main()
