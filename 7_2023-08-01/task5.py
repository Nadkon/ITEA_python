#перехоплення помилки через декоратор

def handle_exception(default_value):
    print('Handle exception')
    def decorator(func):
        print('Handle decorator')

        def wrapper(*args, **kwargs):
            print('Handle wrapper')
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as err:
                print(f'There is an error {err}')
                return default_value

        return wrapper

    return decorator

@handle_exception(default_value=0)
def devide(a, b):
    return a / b

print(devide(10, 0))


