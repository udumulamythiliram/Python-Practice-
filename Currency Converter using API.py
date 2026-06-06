import requests
import sys

from_currency = input("From currency:").upper()
to_currency = input("To currency:").upper()
amount = float(input("Enter amount:"))

API_KEY = "your_API_key_here"

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"

response = requests.get(url)
data = response.json()

if data["result"] != "success":
    sys.exit("Invalid currency code! Please use codes like USD, INR, EUR")

rate = data["conversion_rates"][to_currency]

converted_amount = rate*amount
print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")


