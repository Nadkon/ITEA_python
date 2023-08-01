class A:
    def do_something(self):
        print('Method from A')

class B(A):
    def do_something(self):
        print('Method from B')
        super().do_something()

class C(A):
    def do_something(self):
        print('Method from C')
        super().do_something()

class D(B, C):
    def do_something(self):
        print('Method from D')
        super().do_something()


obj = D()
obj.do_something()
print(D.__mro__)