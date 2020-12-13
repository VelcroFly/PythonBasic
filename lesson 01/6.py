a = float(input('Результат первого дня:'))
b = float(input('Желаемый результат: '))
day_counter = 1

while a < b:
    a += a * 0.1
    day_counter += 1

print(day_counter)
