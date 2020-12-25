"""Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce


def reducer_func(prev_element, current_element):
    return prev_element * current_element


values = [i for i in range(100, 1001) if i % 2 == 0]

a = reduce(reducer_func, values)
print(a)

# values = [1, 2, 3, 1, 10]
#
# a = reduce(reducer_func, values)
# print(a)
