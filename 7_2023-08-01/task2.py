
def sum_closure():
    result = 0
    def inner_sum(y):
        nonlocal result
        result = result + y
        return result
    return inner_sum

func = sum_closure()
#print(func(5))
#print(func(3))
#print(func(10))

def make_average_closure():
    total = 0
    i = 0
    def inner_func(y):
        nonlocal total
        nonlocal i
        total += y
        i += 1
        return total / i
    return inner_func

average_closure = make_average_closure()
print(average_closure(5))
print(average_closure(10))
print(average_closure(15))