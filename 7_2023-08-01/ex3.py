def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure = outer_func(10)

result1 = closure(5)
result2 = closure(8)

print(f'result 1 = {result1}')
print(f'result 2 = {result2}')
