"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError as error:
        print(error)
    return result


def division_v2(a, b):
    try:
        a, b = int(a), int(b)
        res = a / b
    except ValueError:
        return ValueError
    except ZeroDivisionError:
        return ZeroDivisionError
    return round(res, 4)


if __name__ == '__main__':
    print(division(9, 3))
    print(division(9, 0))
    print(division_v2(9, 3))
    print(division_v2(9, 0))
    print(division_v2('a', 'b'))
