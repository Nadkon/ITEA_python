
class MyMeta(type):

    def __new__(mcs, name, bases, dct):
        #Модифікація атрибутів або методіів перед створенням класу
        dct['greeting'] = 'Hello from MyMeta!'
        return super().__new__(mcs, name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
print(obj.greeting)
