camel_name = input("camelCase: ")
print("snake_case: ", end="")
for s in camel_name:
    if s.isupper():
        print("_", s.lower(), sep="", end="")
    else:
        print(s, end="")
