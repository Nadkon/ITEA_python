'''
Напишіть функцію check_password, яка приймає аргумент password і перевіряє, чи є він дійсним паролем.
Уявіть, що дійсний пароль - "password123". Якщо введений пароль збігається, функція повинна повернути True, інакше - False.
'''
def check_password(password):
    if password == 'password123':
        return(True)
    return(False)

#print(check_password('password123'))


'''
Складніший варіант задачі:
Створіть список словників такого виду
[
{'login': 'your login', password: 'your password'},
...
]
в цьому списку кожен елемент буде словником з двома значеннями це логін і пароль.
Далі потрібно створити функцію sign_in яка приймає два параметри login, password. Якщо користувача з таким логіном не існує вертати False, якщо Логін є і парось співпадає повертати True.

В основному скріпті повертати повідомлення користувачу про результат його логіну
'''

password_list = [
{'login': 'dog',
 'password': '123'},
{'login': 'cat',
 'password': '321'},
{'login': 'mouse',
 'password': '555'},
]


def sign_in():
    login_entry = input('login: ')
    password_entry = input('password: ')
    i = 1
    for users in password_list:
        for login in users.values():
            if login == login_entry:
              password = users.get('password')
              if password == password_entry:
                  return("You can entry")
              else:
                  return("Your password in not correct")
            else:
                continue
    return("The user is not exist")

print(sign_in())