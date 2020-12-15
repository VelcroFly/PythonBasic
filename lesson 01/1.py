username = input('Введите имя пользователя:')

while not username:
    print('Ошибка: пустое имя пользователя')
    username = input('Введите имя пользователя:')

print(f'Привет, {username}!')

age = input(f'Сколько тебе полных лет, {username}?')

while not age.isdigit():
    print('Ошибка: возраст должен быть целым числом')
    age = input(f'Сколько тебе полных лет, {username}?')

print(f'Добро пожаловать, {username}! Год твоего рождения {2020 - int(age)}')
