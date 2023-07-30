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

def sign_in(login, password):
  message = 'The user is not exist'
  for user in password_list:
    if user['login'] == login:
      if user['password'] == password:
        message = 'You can entry'
      else:
        message = "Your password is not valid"
  return(message)


login = input('login: ')
password = input('password: ')
print(sign_in(login, password))