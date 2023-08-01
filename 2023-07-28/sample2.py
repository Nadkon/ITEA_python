

class Vehicle:

    def __init__(self, weight, color, places):
        self.weight = weight
        self.color = color
        self.places = places

    def info(self):
        return {
            'weight' : self.weight,
            'color' : self.color,
            'places' : self.places
        }


class Car(Vehicle):

    def __init__(self, *args, marka, year):
        super().__init__(*args)
        self.marka = marka
        self.year = year

    def info(self):
        result = super().info()
        result.update({
            'marka' : self.marka,
            'year' : self.year
        })
        return result

    def __str__(self):
        return f'Car ({self.marka}, {self.year})'




bmw = Car(1500, 'red', 4, marka = 'BMW', year = 2020)

#print(bmw.info())
print (bmw)
