def odd_number_generator():
    index = 1
    def inner():
        nonlocal index
        result = index # щоб повернулася перша 1
        index += 2
        return result
    return inner

odd_gen = odd_number_generator()
for i in range(5):
    print(odd_gen())
