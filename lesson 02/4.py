user_input = input('Введите строку из нескольких слов, разделённых пробелами: ')

for pos, i in enumerate(user_input.split()):
    print(pos, i[:10])



