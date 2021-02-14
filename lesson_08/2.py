"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой."""


class DivisionByZero(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


while True:
    try:
        dividend = int(input('Введите  делимое число: '))
    except ValueError:
        print('Некорректный ввод данных. Попробуйте ещё раз.')
    else:
        break

while True:
    try:
        divider = int(input('Введите  делитель: '))
        if divider == 0:
            raise DivisionByZero('Ошибка: деление на нуль! Попробуйте ещё раз.')
    except (ValueError, DivisionByZero) as err:
        print(err)
    else:
        print(f'{dividend} / {divider} = {dividend / divider}')
        break
