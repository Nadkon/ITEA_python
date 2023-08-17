import math


def factorial(number):
    if number <= 0:
        return 1

    result = math.factorial(number)
    return result

def factorial2(number):
    if number <= 0:
        return 1

    result = 1
    for n in range(1, number+1):
        result *= n
    return result

print(factorial(9))
print(factorial2(9))
