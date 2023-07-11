'''
Напишіть функцію arithmetic_progression_sum, яка приймає аргументи first_term, common_difference і n (кількість членів прогресії) і обчислює суму арифметичної прогресії.
Наприклад, якщо передати first_term = 1, common_difference = 2 і n = 5, функція має повернути суму прогресії: 1 + 3 + 5 + 7 + 9 = 25.
'''

def arithmetic_progression_sum(first_term, common_difference, n):
    result = 0
    rate = 0
    while rate < n:
        result += first_term
        first_term += common_difference
        rate +=1
    return result

print(arithmetic_progression_sum(1, 2, 5))
