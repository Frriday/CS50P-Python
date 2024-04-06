import inflect

list = []
p = inflect.engine()
while True:
    try:
        list.append(input("Name: ").strip())
    except EOFError:
        print()
        break

print("Adieu, adieu, to " + p.join(tuple(list), final_sep=""))
