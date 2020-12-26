"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

numbers_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}

with open('numbers.txt', 'r') as file:
    output_file_content = ''
    for line in file:
        line = line.split(' - ')
        print(line)
        output_file_content += f'{numbers_dict[line[1].strip()]} - {line[1]}'

with open('numbers_output.txt', 'w', encoding='utf-8') as file:
    file.write(output_file_content)
