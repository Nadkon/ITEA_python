#Contect manager via function
from contextlib import contextmanager


@contextmanager
def my_context_manager():
    print('Entering the context')
    try:
        yield
    finally:
        print('Exiting the context')

with my_context_manager():

    print('Doing domething inside the context')
