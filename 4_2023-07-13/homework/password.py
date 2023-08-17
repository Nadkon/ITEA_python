'''
Напишіть програму, яка імпортує модуль string та модуль random. Використовуйте функції цих модулів для генерації випадкового паролю. Попросіть користувача ввести довжину паролю, а потім використайте функцію random.choice для вибору випадкових символів з рядка string.ascii_letters + string.digits. Згенерований пароль виведіть на екран.
'''

import random
import string


def password_generator():
    try:
        entry = int(input('Enter the lengh of the password: '))
        password = ''
        while len(password) < entry:
            password += random.choice(string.ascii_letters + string.digits)
        return password
    except ValueError:
            return('It is not a digit')

print(password_generator())