"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

with open('5.txt', 'w') as file:
    while True:
        user_input = input('Введите число для записи: ')
        if user_input:
            try:
                user_input = float(user_input)
            except ValueError:
                print('Введенное значение не является числом')
                continue
            file.write(f'{user_input} ')
        else:
            break

with open('5.txt', 'r') as file:
    file_content = file.read().split()
    sm = 0
    for i in file_content:
        sm += float(i)

print(sm)
