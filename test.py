"""
This is test file
"""

def odd_number_generator():
    count = 1
    def inner_func():
        nonlocal count
        if count % 2 != 0:
            result = count
        else:
            return False
        count +=1
        return result
    return inner_func


odd_gen = odd_number_generator()
for i in range(5):
    print(odd_gen())
