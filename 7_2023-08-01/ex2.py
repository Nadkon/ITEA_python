def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def math_operation(operation, a, b):
    return operation(a, b)

#print(math_operation(add, 3, 5))


def get_math_operation(operation):
    if operation == 'add':
        return add
    elif operation == 'substract':
        return substract
    elif operation == 'multiply':
        return multiply

operation_func = get_math_operation('substract')
result = operation_func(4, 5)

print(result)