'''
Напишіть програму, яка імпортує модуль datetime і використовує його функції для отримання поточної дати та часу. Виведіть на екран поточну дату та час у зрозумілому форматі.
'''

import datetime

now = datetime.datetime.now()
date_time = now.strftime("%d %B %Y, %I:%M")
print(f'Now is {date_time}')
