import requests
import sys


while True:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        msg = response.json()
        rate = float(msg["bpi"]["USD"]["rate_float"])
        if len(sys.argv) != 2:
            raise ValueError
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Common-line arguement is not a number")
    except requests.RequestException:
        sys.exit("Request Failed")
    else:
        print(f"${n * rate:,.4f}")
        break
