from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Square(Shape):
    def __init__(self, sside_length):
        self.side_length = sside_length

    def area(self):
        return self.side_length**2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


# Не можна створити обєкт абстрактного класу
#shape = Shape()
circle = Circle(5)
square = Square(4)

print(circle.area())
print(square.area())

