from itertools import count, cycle
from sys import argv

"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

"""
params: a 3 10
params: b 10 10 35 21 58 63
"""

if argv[1] == 'a':
    for i in count(int(argv[2])):
        if i > int(argv[3]):
            break
        else:
            print(i)
elif argv[1] == 'b':
    repeat_counter = 0
    for i in cycle(argv[3:]):
        repeat_counter += 1
        if repeat_counter < int(argv[2]) * len(argv[3:]):
            print(i)
        else:
            break
else:
    pass


