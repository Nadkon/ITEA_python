'''
Напишіть функцію is_prime, яка приймає аргумент num і перевіряє, чи є число простим.
Число вважається простим, якщо воно ділиться лише на 1 і на самого себе. Функція має повернути True, якщо число є простим, і False - в іншому випадку.
'''

def is_prime(num):
    prime = True
    i = 2
    while i <= num ** (0.5):
        if num % i == 0:
            prime = False
            break
        i += 1
    return prime

num = int(input('Enter a number: '))
print(is_prime(num))