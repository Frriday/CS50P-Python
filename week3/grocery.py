dict = {}
while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        for key, value in sorted(dict.items()):
            print(f"{value} {key}")
        break
    else:
        if item in dict:
            dict[item] += 1
        else:
            dict = dict | {item : 1}
