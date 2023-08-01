#polymorphism

class Shape:
    ...


class Circle(Shape):
    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Rectabgle(Shape):
    def calculate_are(self):
        return self.width * self.height


