import re



def convert(hour):
    if matches := re.search("^([0-9]{1,2})(?::([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)$", hour):
        time = matches.groups()
        s_hour, s_minute, s_flag, e_hour, e_minute, e_flag = time

        if s_minute is None:
                s_minute = 0

        if e_minute is None:
            e_minute = 0

        s_hour = int(s_hour)
        s_minute = int(s_minute)
        e_hour = int(e_hour)
        e_minute = int(e_minute)

        if (
            s_hour > 12 or s_hour < 0 or
            s_minute > 59 or s_minute < 0 or
            e_hour > 12 or e_hour < 0 or
            e_minute > 59 or e_minute < 0
        ):
            raise ValueError
        if s_flag == "PM" and s_hour == 12:
            s_hour = 12
        elif s_flag == "PM" and s_hour != 12:
            s_hour += 12
        elif s_flag == "AM" and s_hour == 12:
            s_hour = 0;

        if e_flag == "PM" and e_hour == 12:
               e_hour = 12
        elif e_flag == "PM" and e_hour != 12:
             e_hour += 12
        elif e_flag == "AM" and e_hour == 12:
            e_hour = 0

        return f"{s_hour:02d}:{s_minute:02d} to {e_hour:02d}:{e_minute:02d}"
    else:
        raise ValueError

def main():
    time = input("Hours: ")
    print(convert(time))


if __name__ == "__main__":
    main()
