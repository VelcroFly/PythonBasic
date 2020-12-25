def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < c and b < c:
        return c + a
    else:
        return a + b


def my_func_v2(a, b, c):
    my_list = [a, b, c]
    try:
        my_list.remove((min(my_list)))
        return sum(my_list)
    except TypeError:
        return TypeError


if __name__ == '__main__':
    print(my_func(1, 2, 3))
    print(my_func(1, 3, 2))
    print(my_func(9, 2, 4))
    print(my_func(9, 4, 2))
    print(my_func(4, 7, 1))
    print(my_func(4, 1, 7))
    print(my_func_v2(1, 2, 3))
    print(my_func_v2(1, 3, 2))
    print(my_func_v2(9, 2, 4))
    print(my_func_v2(9, 4, 2))
    print(my_func_v2(4, 7, 1))
    print(my_func_v2(4, 1, 7))

