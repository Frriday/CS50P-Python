months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    date = date.split(",")
    try:
        if len(date) == 2:
            year = date[1].strip()
            month, day = date[0].split()
            month = months.index(month) + 1
        else:
            month, day, year = date[0].split("/")
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        pass
    else:
        if (month < 0 or month > 12) or (day > 31):
            continue
        print(f"{year:>04}-{month:>02}-{day:>02}")
        break
