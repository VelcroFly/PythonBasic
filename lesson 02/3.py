month = str()

while True:
    month = input('Введите месяц в виде целого числа от 1 до 12: ')

    try:
        month = int(month)
    except ValueError:
        print('Ошибка ввода! Введите месяц в виде целого числа от 1 до 12:')
        continue

    if month < 1 or month > 12:
        print('Ошибка ввода! Введите месяц в виде целого числа от 1 до 12:')
        continue
    else:
        break

seasons_dict = {'зимой': [12, 1, 2],
                'весной': [3, 4, 5],
                'летом': [6, 7, 8],
                'осенью': [9, 10, 11]
                }

for season, months_in_season in seasons_dict.items():
    if month in months_in_season:
        print(f'Это месяц {season}!')

