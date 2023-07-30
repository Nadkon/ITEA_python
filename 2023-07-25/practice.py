names = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j']

myList = [{'id' : index, 'name' : name} for index, name in enumerate(names)]

print(myList)

import json
with open ('test.json', 'w') as file:
    json.dump(myList, file)