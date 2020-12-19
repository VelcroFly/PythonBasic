my_list = [1, '2', True, [1, 2], (3, 4), {'1 2 3'}, b'123', bytearray(b'321'), {'key': 'value'}, None]

for position, value in enumerate(my_list):
    print(position, type(value))
