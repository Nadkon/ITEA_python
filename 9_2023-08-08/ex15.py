def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)

print(countdown(5))#нічого не поверне бо числа, які генерувалися, не зберігаються у памяті

numbers = list(countdown(5))
print(numbers) #А ось так збережеться тому що ми перевели його у список і змогли зберігти


def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a , b = b, a + b
        count +=1

for num in fibonacci_generator(10):
    print(num)
