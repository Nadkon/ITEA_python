'''
Запишіть своє ім'я в змінну name і виведіть його на екран разом з привітанням "Привіт, [ім'я]!". Перед виведенням на екран результату перевірте змінну name на наявність в ній чисел або інших спец символів. Ім'я повинне містити тільки літери та почитися з великої літери.
'''
my_name = input('Enter your name: ')

isDigit = False
for char in my_name:
    if char.isdigit():
       isDigit = True

if isDigit == True:
    print ('Your name is invalid. Please write correct name')
else:
    checked_name = my_name.lower()
    print(f'Hello, {checked_name.capitalize()}!')
