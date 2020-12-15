number = int(input('Введите целое положительное число:'))
max_value = number % 10

while number > 0:
    number = number // 10
    current_value = number % 10
    if current_value > max_value:
        max_value = current_value

print(max_value)
