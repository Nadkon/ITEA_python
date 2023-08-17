from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Car(ABC):

    wheels: int = None
    motor_v: float = None
    weight: float = None

# Базовий метод
    def get_wheels(self):
        return self.wheels

# Абстрактний метод який потрбіно реалізувати у кожного нащадка від цього класу
    @abstractmethod
    def get_speed(self):
        pass


class SportCar(Car):

    def get_speed(self):
        return 100 * self.weight / self.motor_v

    def get_wheels(self):
        return('Number for lamborgini')

class SHCar(Car):

   def get_speed(self):
      return 10 * self.weight / self.motor_v



labmorgini = SportCar(wheels=4, motor_v=5, weight=700)
traktor = SHCar(wheels=8, motor_v=16, weight=5000)

print(labmorgini.get_speed())
print(traktor.get_speed())
print(labmorgini.get_wheels())
print(traktor.get_wheels())


#Ще приклад
def get_info(car: Car):
    return {
        'wheels': car.wheels,
        'speed': car.get_speed
        }
if __name__ == '__main__':
    labmorgini = SportCar(wheels=4, motor_v=5, weight=700)
    traktor = SHCar(wheels=8, motor_v=16, weight=5000)
    print(get_info(car=labmorgini))
    print(get_info(car=traktor))
