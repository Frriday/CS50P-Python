import re


def validate(ip):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        list = ip.split(".")
        for i in list:
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    else:
        return False


def main():
    ip = input("IPv4 Address ").strip()

    print(validate(ip))


if __name__ == "__main__":
    main()
