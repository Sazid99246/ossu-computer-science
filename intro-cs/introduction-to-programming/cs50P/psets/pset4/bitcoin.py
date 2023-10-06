import requests
import sys
import json

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    elif (len(sys.argv) > 1 ):
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        output = response.json()

        rateFloat = output["bpi"]["USD"]['rate_float']

        perCoin = rateFloat * float(sys.argv[1])
        print(f"${perCoin:,.4f}")

except requests.RequestException:
    sys.exit()