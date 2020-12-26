"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('input.txt', 'r', encoding='utf-8') as file:
    line_counter = 0
    for line in file:
        line_counter += 1
        words_in_line = len(line.split())
        print(f'{line_counter}: "{line.strip()}". Строка содерит {str(words_in_line)} элементов.')

