from dataclasses import dataclass


@dataclass
class Square2:

    def __init__(self, position: tuple[int, int], color: str = 'red'):
        position: self.position



@dataclass
class Square:

    position: tuple[int, int]
    #analog of
    #def __init__(self, position: tuple[int, int]):
    # position: self.position

    color: str = 'red'

s = Square(position=(1, 1))

print(s)


