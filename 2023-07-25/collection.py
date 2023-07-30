from collections import Counter

fruits = ['apple', 'apple', 'banana', 'banana', 'grape']
fruit_counter = Counter(fruits)

print(fruit_counter['apple'])
print(fruit_counter['banana'])
print(fruit_counter['grape'])
print(fruit_counter['cake'])
print(fruit_counter)
print(fruit_counter.total)
print(fruit_counter.most_common(2))
