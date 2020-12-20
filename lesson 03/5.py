def fn():
    overall_result = int()
    status = True
    while status:
        current_result = int()
        user_input = input('Введите строку чисел, разделенных пробелом: ')
        values_list = user_input.split()
        for value in values_list:
            try:
                value = float(value)
                current_result += value
                overall_result += value
            except ValueError:
                if value == 'q':
                    status = False
                else:
                    pass
        yield current_result, overall_result


if __name__ == '__main__':
    a = fn()
    for i in a:
        print(i)
