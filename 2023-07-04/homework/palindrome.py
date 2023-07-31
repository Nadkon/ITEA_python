'''
Напишіть функцію is_palindrome, яка приймає аргумент word і перевіряє, чи є це слово паліндромом.
Паліндром - це слово, яке читається однаково зліва направо і справа наліво. Функція має повернути True, якщо слово є паліндромом, і False - в іншому випадку.
'''

def is_palindrome(word):
    palindrome = ''
    i = len(word)
    while i > 0:
        i -= 1
        palindrome += word[i]
    if word.lower() == palindrome.lower():
        return True
    else:
        return False

def is_palindrome2(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False

def is_palindrome3(word):
    return word.lower() == word[::-1].lower()


print(is_palindrome3('Anna'))
#print(is_palindrome('Anna'))