def log_method(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class MyClass:

    @log_method
    def my_method(self, x):
        return x * 2


obj = MyClass()
result = obj.my_method(5)
print(result)


