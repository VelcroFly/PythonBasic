def division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError as error:
        print(error)
    return result


if __name__ == '__main__':
    print(division(9, 3))
    print(division(9, 0))
