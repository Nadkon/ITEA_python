'''
Напишіть програму, яка конвертує суму введену користувачем з однієї валюти в іншу. Користувач повинен ввести суму, вихідну валюту (наприклад, USD, EUR, UAH) та цільову валюту (наприклад, USD, EUR, UAH). За допомогою оператора "if" визначте курс конвертації для валют та виведіть сконвертовану суму.
'''

currency_uah = {
    'usd': 36.6,
    'eur': 39.7
}
currency_usd = {
    'uah': 36.6,
    'eur': 0.92
}

currency_eur = {
    'uah': 39.7,
    'eur': 1.09
}


try:
    your_input = int(input('Enter a number: '))
    from_currency = input('Enter a currency to change: ')
    to_currency = input('Enter a currency which you would like to receive: ')

    if from_currency.lower() == 'uah':
        if to_currency != 'usd' and to_currency != 'eur':
            print(f'You cannot change from {from_currency} to {to_currency}')
        else:
            result = round (your_input / currency_uah[to_currency], 2)
            print (result)
    elif from_currency.lower() == 'usd':
        if to_currency != 'uah' or to_currency != 'eur':
            print(f'You cannot change from {from_currency} to {to_currency}')
        else:
            result = round (your_input / currency_usd[to_currency], 2)
            print (result)
    elif from_currency.lower() == 'eur':
        if to_currency != 'usd' or to_currency != 'uah':
            print(f'You cannot change from {from_currency} to {to_currency}')
        else:
            result = round (your_input / currency_eur[to_currency], 2)
            print (result)
    else:
        print("Please check the currency name")
except ValueError:
    print('It is not a number')

