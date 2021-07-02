currencies = "EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel \
|GBP - United Kingdom Pound |DKK - Denmark Krone |CAD - Canada Dollar |JPY - Japan Yen |HUF - Hungary Forint \
|RON - Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |SGD - Singapore Dollar |HKD - Hong Kong Dollar \
|AUD - Australia Dollar |CHF - Switzerland Franc |KRW - Korea (South) Won |CNY - China Yuan Renminbi |TRY - Turkey Lira \
|HRK - Croatia Kuna |NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States Dollar |NOK - Norway Krone \
|RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso |CZK - Czech Republic Koruna |BRL - Brazil Real \
|PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand"

list_of_currencies = currencies.split(" |")

def currency_codes():
    for i in list_of_currencies:
        print(i)

from forex_python.converter import CurrencyRates

c = CurrencyRates()

z = input("Type ls to show the list of currency codes. Press anything else to continue..\n")
if z == "ls":
    currency_codes()

print("\n---Welcome to currency exchange portal---\n")
amount = int(input("Enter the amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

conversion_rate = c.get_rate(from_currency, to_currency)
result = c.convert(from_currency, to_currency, amount)

print(f"The conversion rate is: 1 {from_currency} = {conversion_rate} {to_currency}")
print(f"{amount} {from_currency} = {result} {to_currency}")

