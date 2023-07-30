print("Hello! I'm calculator. Give me 'a' and 'b' numbers. I'll send you div")

a, b = None, None

attempt = 1
while True:
    try:
        if attempt > 3:
            raise Exception("Sorry, it was last attempt") # Цей запис зупине програму із помилкою
        a = int(input('Input real digit for a: '))
    except ValueError as error:
        print('It is not a digit. Input real digit: ')
        attempt += 1
        continue
    else:
        break

while attempt > 3:
    try:
        b = int(input("Input real digit for b: "))
    except ValueError as error:
        print('Input real digit')
        continue
    else:
        break

try:
    result = a / b
except ZeroDivisionError as error:
    print("Sorry, we can't divide by zero")
else:
    print(f'Result {a} / {b} = {result}')
finally:
    print('Good bye!')


