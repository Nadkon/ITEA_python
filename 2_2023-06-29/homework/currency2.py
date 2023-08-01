uah_eur = 38
uah_usd = 39
eur_usd = 88

try:
    your_input = int(input('Enter a value: '))
    from_currency = input('Enter the currency you would you like to change: ')
    to_currency = input('Enter a currency which you would like to receive: ')
    result = 0

    if from_currency.lower() == 'uah':
        if to_currency.lower() == 'eur':
            result = round((your_input / uah_eur), 2)
        if to_currency.lower() == 'usd':
            result = round((your_input / uah_usd), 2)

    elif from_currency.lower() == 'eur':
        if to_currency.lower() == 'usd':
            result = round((your_input / eur_usd), 2)
        if to_currency.lower() == 'uah':
            result = round((your_input * uah_eur), 2)

    elif from_currency.lower() == 'usd':
        if to_currency.lower() == 'eur':
            result = round((your_input * eur_usd), 2)
        if to_currency.lower() == 'uah':
            result = round((your_input * uah_usd), 2)
    elif result == 0:
        print("Please check the currency name")
except ValueError:
  print("Check your entry")