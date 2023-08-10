class MathOperations:

    multiplier = 2

    def __init__(self, value):
        self.value = value


    @staticmethod
    def add(a, b):
        return a + b


    @classmethod
    def multiply(cls, x):
        return cls.multiplier * x


result = MathOperations.add(3, 5)
print(f'The first result is {result}')
obj = MathOperations(5)
result = obj.multiply(3)
print(f'The second result is {result}')
result = obj.add(3, 5)
print(f'The third result is {result}')
