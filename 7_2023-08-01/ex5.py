
def my_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def say_hello():
    print('Hi!')

say_hello = my_decorator(say_hello)

# або ось так. Так більш локанічно
@my_decorator
def say_bye():
    print('Bye!')

say_hello()
say_bye()