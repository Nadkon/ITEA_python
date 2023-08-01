a, b = None, None
attempt = 1
while True:
    try:
        if attempt > 3:
            raise Exception ('It was last attempt!')
        a = int(input('enter a'))
    except ValueError as error:
        print('It is not a digit')
        attempt += 1
        continue
    else:
        break

while True:
    try:
        b = int(input('enter b'))
    except ValueError as error:
        print('It is not a digit')
        continue
    else:
        break


# Подивитися що там далі наисано у коді
print (a + b)