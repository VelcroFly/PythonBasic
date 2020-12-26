"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open('input.txt', 'w', encoding='utf-8') as file:
    while True:
        user_input = input('Введите данные для записи в файл: ')
        if user_input:
            file.write(user_input + '\n')
        else:
            print('Запись завершена!')
            break

