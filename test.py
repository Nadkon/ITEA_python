class CarSaver:
    def save_car(self, car, car_type):
        if car_type == "electric":
            self.save_to_electric_db(car)
        elif car_type == "gasoline":
            self.save_to_gasoline_db(car)
        elif car_type == "diesel":
            self.save_to_diesel_db(car)

    def save_to_electric_db(self, car):
        # Збереження даних електричного автомобіля в базу даних
        pass

    def save_to_gasoline_db(self, car):
        # Збереження даних автомобіля з бензиновим двигуном в базу даних
        pass

    def save_to_diesel_db(self, car):
        # Збереження даних дизельного автомобіля в базу даних
        pass

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

electric_car = Car("Tesla", "Model 3", 2023)
gasoline_car = Car("Toyota", "Camry", 2023)
diesel_car = Car("Ford", "F-150", 2023)

car_saver = CarSaver()
car_saver.save_car(electric_car, "electric")
car_saver.save_car(gasoline_car, "gasoline")
car_saver.save_car(diesel_car, "diesel")