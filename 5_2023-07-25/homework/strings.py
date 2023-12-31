'''
Напишіть функцію, яка приймає список рядків та обертає ті з них, які містять лише великі літери. Решта рядків повертає без змін.


Приклад:
Input: ["hello", "WORLD", "Python", "UPPERCASE"]
Очікуваний результат: ['hello', 'DLROW', 'Python', 'ESACREPPU']
'''

def string_for_reverse(input):
    i = 0
    for item in input:
        if item == item.upper():
            input[i] = item[::-1]
            i += 1
        else:
            i += 1
            continue
    return input

print(string_for_reverse(["hello", "WORLD", "Python", "UPPERCASE"]))

def string_for_reverse2(input):
    newlist = [item if item.upper() != item else item[::-1] for item in input]
    return newlist


print(string_for_reverse2(["hello", "WORLD", "Python", "UPPERCASE"]))
    #newlist = [x if x != "banana" else "orange" for x in fruits]

