vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
msg = input("Input: ")
print("Output: ", end="")
for s in msg:
    if s not in vowels:
        print(s, end="")
