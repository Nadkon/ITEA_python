'''
Напишіть програму, яка імпортує модуль math і використовує його функції для виконання простих обчислень. Попросіть користувача ввести радіус кола і обчисліть його площу за допомогою функції math.pi та формули площа = pi * радіус^2. Виведіть результат на екран.
'''

import math

def circle_area():
  try:
    radius = int(input('Enter a circle radius: '))
    area = math.pi * (radius**2)
    return round(area, 2)
  except ValueError:
    return ('Your entry is not a digit')

print(circle_area())