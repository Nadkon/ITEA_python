def square(x):
    return x * x

square_lambda = lambda x: x * x


def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y

numbers = [1,2,3,4,5]

square_numbers = map(lambda x: x * x, numbers)
print(list(square_numbers))


even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

people = [
{'name': 'John', 'age': 30}
{'name': 'Nadine', 'age': 40}
]

people.sort(key=lambda person: person['age'])
#тут key це параметр для функції sort. Тобто показує по якому зченню dic мені фільтрувати
print(people)
