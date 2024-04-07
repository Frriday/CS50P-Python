def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    l = len(plate)
    if 2 <= l <= 6:
        for i in range(l):
            if plate[i].isnumeric():
                plate_front = plate[0:i]
                plate_behine = plate[i:l]
                return (len(plate_front) >= 2) and (not plate_behine.startswith("0")) and (plate_behine.isdecimal())
    else:
        return False
    return True


if __name__ == "__main__":
    main()
