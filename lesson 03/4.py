def my_func(x, y):
    return x ** y


def my_func_v2(x, y):
    divider = 1
    while y < 0:
        divider *= x
        y += 1
    return 1 / divider


if __name__ == '__main__':
    print(my_func(4, -2))
    print(my_func_v2(4, -2))
    print(my_func(2, -3))
    print(my_func_v2(2, -3))
    print(my_func(14, -35))
    print(my_func_v2(14, -35))
