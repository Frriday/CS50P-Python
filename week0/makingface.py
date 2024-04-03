def convert(feeling):
    feeling = feeling.replace(':)', '🙂')
    feeling = feeling.replace(':(', '🙁')
    return feeling


def main():
    feeling = input("How do you feel today? ")
    print(convert(feeling))


main()
