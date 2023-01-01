import requests

class Currency:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data["rates"]
        
    def convert(self, from_currency, to_currency, amount):
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]
            
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
    
amount = 100
from_currency = "USD"
to_currency = "AUD"

currency = Currency("https://api.exchangerate-api.com/v4/latest/USD")
response = "{:,.2f}".format(currency.convert(from_currency, to_currency, float(amount)))

print(amount, from_currency, "to", to_currency, "is", response)

