# на замиканні
def fibonacci_generator():
    a, b = 0, 1
    def inner():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return (result)
    return inner


fib_gen = fibonacci_generator()
for i in range(10):
     print(fib_gen())
     
