temperature = int(input('Enter temperature '))
#зробити перевірку на номер
unit = input('Enter metric ')

if unit.lower() == 'f':
    print (f'The temperature is {(temperature - 32)* 5/9}C')
elif unit.lower() == 'c':
    print (f'The temperature is {(temperature * 9/5)+32}F')
else:
    print ('Your input is not correct')
