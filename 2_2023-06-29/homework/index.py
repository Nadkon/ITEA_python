'''
Напишіть програму, яка зчитує вагу (у кілограмах) та зріст (у метрах) користувача і обчислює його ІМТ. Виведіть повідомлення згідно наступним критеріям:
ІМТ менше 18.5: "Недостатня маса тіла"
ІМТ від 18.5 до 24.9: "Нормальна маса тіла"
ІМТ від 25 до 29.9: "Надлишкова маса тіла"
ІМТ більше 29.9: "Ожиріння"
'''
weight = input ('Enter your weight: ')
height = input('Enter your height in cm: ')

try:
    weight = int(weight)
    height = int(height)
except:
    print('Your entry is not correct')
else:
    index = (weight / (height/100)**2)
    print (index)
    if index < 18.5:
        print('Недостатня маса тіла')
    elif index < 24.9:
        print('Нормальна маса тіла')
    elif index < 29.9:
        print('Надлишкова маса тіла')
    else:
        print('Ожиріння')