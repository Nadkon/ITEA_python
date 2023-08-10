class Singleton:
    _instance = None

    def __new__(cls, *argss, **kwargs):
        print('Method New')
        print(cls._instance)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        print('----------------')
        return cls._instance


obj1 = Singleton('some text')
obj2 = Singleton('additional text')
obj3 = Singleton('additional text')


print(obj1 is obj2)
