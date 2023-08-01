from collections import defaultdict

fruits_counter = defaultdict(int)
fruits = ['apple', 'apple', 'banana', 'banana', 'grape']
print(fruits_counter)

for fruit in fruits:
    fruits_counter[fruit] +=1

print(fruits_counter)