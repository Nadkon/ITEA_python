from abc import ABC, abstractmethod

class Car(ABC):
    def save_car(self):
        pass

class Electric(Car):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def save_car(self):
        # Збереження даних електричного автомобіля в базу даних
        pass


class Gasoline(Car):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def save_car(self):
        # Збереження даних автомобіля з бензиновим двигуном в базу даних
        pass


class Diesel(Car):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def save_car(self):
        # Збереження даних дизельного автомобіля в базу даних
        pass

electric_car = Electric("Tesla", "Model 3", 2023)
gasoline_car = Gasoline("Toyota", "Camry", 2023)
diesel_car = Diesel("Ford", "F-150", 2023)
