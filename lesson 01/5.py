gain = float(input('Введите размер выручки: '))
expense = float(input('Введите размер издержек: '))

if gain > expense:
    print(f'Фирма получает прибыль в размере {gain - expense}')
    print(f'Рентабельность выручки: {gain / expense}')
    number_of_employees = int(input('Введите кол-во сотрудников фирмы: '))
    print(f'Прибыль на одного сотрудника: {(gain - expense) / number_of_employees}')
elif gain < expense:
    print(f'Убыток фирмы равен {expense - gain}')
else:
    print('Выручка фирмы равна сумме издержек')
