from abc import ABC, abstractmethod

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):
                total_area += shape.width + shape.height
          #Якщо зявиться новий тип фігури то метод потрібно буде модифікувати!!!!


# А ось так як нижче нічого не потрбіно буде редагувати, лише прописати метод у новій фігурі

class Shape(ABC):
    @abstractmethod
    def calculate_area2(shape):
        pass


class Rect2(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area2(self):
        return self.width * self.height

class AreaCalculator:

    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.calculate_area2()

