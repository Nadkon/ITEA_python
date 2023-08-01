class Person:

    def __init__(self, name, surename,age):
        self.name = name
        self.surename = surename
        self.age = age

    def walk(self):
        return("I'm walking")

    def eat(self):
        return("I'm eating")

    def sleep(self):
        return("I'm sleeping")

    def work(self):
        return("I'm working")

person = Person('Nadiia', 'Konon', 42)

print(person.walk())