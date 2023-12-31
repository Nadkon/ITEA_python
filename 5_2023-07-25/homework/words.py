'''
Напишіть функцію, яка приймає текст та повертає словник, де ключі - слова, а значення - кількість їх входжень у тексті. Врахуйте ігнорування регістру та пунктуації.

Приклад:
Input: "Це це тестовий текст. Тестовий текст для тестування. Тест!"
Очікуваний результат: {'це': 2, 'тестовий': 2, 'текст': 2, 'для': 1, 'тестування': 1, 'тест': 1}
'''

from collections import Counter


def word_count(text):
    word_counter = Counter(text.lower().replace('.', '').replace(',', '').replace('!', '').split())
    return word_counter

print(word_count('Це це тестовий! текст. Тестовий, текст! для, тестування. Тест'))
