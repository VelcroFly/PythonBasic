a = float(input('Результат первого дня:'))
b = float(input('Желаемый результат: '))
day_counter = 1

while a < b:
    print(f'{day_counter}-й день - дистанция {a:.2f}')
    a += a * 0.1
    day_counter += 1

print(f'Через {day_counter} дней спортсмен достгнет результата не менее, чем {b} км')
