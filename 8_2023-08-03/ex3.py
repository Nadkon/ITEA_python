import functools


@functools.lru_cache
def some_function(*args):
    return sum(args)


print(some_function(1,2,3))
print(some_function(1,2,3,4))
print(some_function(1,2,3))



def my_decorator(func):

  #@wraps(func)
  def wrapper(*args, **kwargs):
     print ('Hello')
     return func(*args, **kwargs)
  return wrapper

@my_decorator
def say_hello():
   print('Hi')

say_hello()
print(say_hello.__name__)
print(say_hello.__doc__)
#губляться метадані. Томущо ми вертаємо нову функцію з врапера.
# Тому краще використовувати вбудований врапер імпортований з functools - див вище у коменті wraps(func)
# якщо розкоментувати то помилка виправиться
