# Context Manager via class

class MyContextManager:

    def __enter__(self):
        print('Entering the context')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting the context')

    def do_something(self):
        print('Doing something inside the context')


with MyContextManager() as cm:
    cm.do_something()