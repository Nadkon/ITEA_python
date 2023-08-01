person = {'name' : 'Nadiia', 'age': 31}

print(person['name'])

person['name'] = "Sveta"

print(person.get('something', 'default'))

keys = ['name', 'surname']
person1 = dict.fromkeys(keys, 'no info')

print(person1)

print(person.keys())
print(person.values())
print(person.items())

for key, value in person.items():
    print(key, value)

