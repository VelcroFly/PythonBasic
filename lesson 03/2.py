def print_fn(name, lastname, birth, city, email, phone):
    return print(f'{name} {lastname} {str(birth)} {city} {email} {phone}')


if __name__ == '__main__':
    print_fn(name='John', lastname='Smith', birth=1976, city='NY', email='smith@gmail.com', phone='3335566')
