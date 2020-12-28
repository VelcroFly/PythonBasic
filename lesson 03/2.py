def print_fn(name, lastname, birth, city, email, phone):
    return print(f'{name} {lastname} {birth} {city} {email} {phone}')


def print_fn_v2(**kwargs):
    return ' '.join(kwargs.values())


if __name__ == '__main__':
    print_fn(name='John', lastname='Smith', birth='1976', city='NY', email='smith@gmail.com', phone='3335566')
    print(print_fn_v2(name='John', lastname='Smith', birth='1976', city='NY', email='smith@gmail.com', phone='3335566'))
