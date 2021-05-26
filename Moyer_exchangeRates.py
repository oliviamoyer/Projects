# Olivia Moyer
# 001

# import statements
import requests

# global variables

CURRENCY = ['CAD', 'HKD', 'ISK', 'PHP', 'DKK', 'HUF', 'CZK', 'GBP', 'RON', 'SEK', 'IDR', 'INR', 
'BRL', 'RUB', 'HRK', 'JPY', 'THB', 'CHF', 'EUR', 'MYR', 'BGN', 
'TRY', 'CNY', 'NOK', 'NZD', 'ZAR', 'MXN', 'SGD', 'AUD', 'ILS', 'KRW', 'PLN', 'USD']

COUNTRY = ['Canada', 'Hong Kong', 'Iceland', 'Philippines', 'Denmark', 'Hungary', 'Czechia', 'United Kingdom', 'Romania', 'Sweden', 'Indonesia', 'India', 
'Brazil', 'Russia', 'Croatia', 'Japan', 'Thailand', 'Switzerland', 'European Union', 'Malaysia', 'Bulgaria',
'Turkey', 'China', 'Norway', 'New Zealand', 'South Africa', 'Mexico', 'Singapore', 'Australia', 'Israel', 'South Korea', 'Poland', 'United States' ]
        
URL = "https://api.exchangeratesapi.io/latest" # currency exchange rates w base of EUR

# function definitions
def getURLdata(url,options=''): # find resturant and what is it that you want 
    try:
        response = requests.get(url,options)
        if response.status_code != 200:
            raise
        data = response.json()
        return data
    except:
        print("API call was not successful.")
        return None

# validating amount
def strtonum(x):
    try:
        if x.isdigit():
            return (True, int(x))
        else:
            return (False, "xxx")
    except:
        return (False, "xxx")

# validating currency code/country
def currencycode(y):
    y=y.upper()
    if y in CURRENCY:
        return y
    else: 
        y=y.lower()
        y=y.title()
        if y in COUNTRY:
            place=COUNTRY.index(y)
            code=CURRENCY[place]
            return code
        else:
            return "XXX"


# application code
# user input
while True:
    userin=input("Convert an amount? Type Yes or No:",)
    userin=userin.lower()
    if userin=="no":
        break
    userinamount=input("Enter your amount:", )
    userinbase=input("Currency code or country of amount:", )
    userinchange=input("Currency code or country for conversion:", )

    # checking user input
    (valid, amount)=strtonum(userinamount)
    basecheck=currencycode(userinbase)
    convertcheck=currencycode(userinchange)

    # conversion
    if basecheck!="XXX" and convertcheck!="XXX" and valid: 
        opt={'base': basecheck}
        currencyData=getURLdata(URL, opt)
        rates=(currencyData['rates'])
        convertrate=(rates[convertcheck])
        conversion=amount*convertrate
        print('Your converted amount is {:,.2f} in {} currency'.format(conversion, convertcheck))
    else: 
        print("You have provided invalid input.")