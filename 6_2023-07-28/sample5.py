# Encapsulation

class Parent:
    def __init__(self):
        self._protected_var = 10

    def _protected_method(self):
        return self._protected_var * 2

    def __private_method(self):
        return self._protected_var ** 2



class Child(Parent):

    def get_protected_var(self):
        return self._protected_var  #можна звертатися до захищенного поля у підкласі



child = Child()

print(child.get_protected_var())  # виведе 10
print(child._protected_method())  # виведе 20. Але так неправильно звертатися і краще так не рообити
#print(child.__private_method())  # виведе Error
print(child._Parent__private_method())  # виведе 100. Тобто ось так зможемо достукатися
