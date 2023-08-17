# на замиканні
def fibonacci_generator():
    a, b = 0, 1
    count = 1
    def inner():
        nonlocal a, b, count
        result = a
        a, b = b, a + b
        print(f"Count# {count}: a = {a}, b = {b}")
        count +=1
        return (result)
    return inner


fib_gen = fibonacci_generator()
for i in range(10):
     print(fib_gen())

