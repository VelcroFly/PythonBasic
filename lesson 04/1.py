"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""
from sys import argv


def salary(params):
    try:
        hours, base, bonus = int(params[0]), int(params[1]), int(params[2])
        return hours * base + bonus
    except ValueError:
        return ValueError
    except TypeError:
        return TypeError


def unpack_args():
    try:
        hours, base, bonus = argv[1:]
        return hours, base, bonus
    except ValueError:
        return ValueError


print(salary(unpack_args()))
