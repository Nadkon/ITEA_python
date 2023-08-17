from abc import ABC, abstractmethod

class Bird:

    def fly(self):
        pass

class Ostrich(Bird):

    def fly(self):
        raise Exception("Ostrich can't fly")


def make_bird_fly(bird):
    bird.fly()  #У випадку з Ostrich виникне Exception


#А ось так краще
class Bird2(ABC):

    @abstractmethod
    def fly(self):
        pass

class Ostrich2(Bird2):

    def fly(self):
        return False



def make_bird_fly2(bird):
    if bird.fly():
        print('Flying')
    else:
        print("Can't fly" )