import random

num = 0
while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
    except ValueError:
        pass
    else:
        num = random.randint(1, level)
        break



while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            raise ValueError
    except ValueError:
        pass
    else:
        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            print("Just right!")
            break
