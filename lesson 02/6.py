help_description = """Меню программы:
\t1. Добавить товар
\t2. Просмотреть товары
\t3. Показать аналитику
\t4. Загрузить тестовые данные
\t5. Просмотреть помощь
\t0. Выйти"""

print(help_description)
choice = ''
shop_items = []


while choice != '0':
    choice = input('Выберите действие из меню("5" - помощь): ')

    if choice == '1':
        title = input('Введите название: ')
        price = input('Введите цену: ')
        amount = input('Введите количество товара: ')
        unit = input('Введите единицы измерения: ')
        product = {'название': title,
                   'цена': price,
                   'количество': amount,
                   'eд': unit}
        shop_items.append(((len(shop_items) + 1), product))
        print('Товар добавлен!')

    if choice == '2':
        product_description = str()

        for i in shop_items:
            for key in i[1].keys():
                product_description += f'{key}: {i[1].get(key)}; '
            product_description += '\n'

        print(product_description)

        # for i in shop_items:
        #     print(f"{i[0]}: {i[1].get('название')}, цена: {i[1].get('цена')}, кол-во: {i[1].get('количество')} "
        #           f"{i[1].get('eд')}")

    if choice == '3':
        analysis_dict = dict()

        for product in shop_items:
            for i in product[1].items():
                if i[0] not in analysis_dict.keys():
                    analysis_dict[i[0]] = []
                    analysis_dict[i[0]].append(i[1])
                else:
                    analysis_dict[i[0]].append(i[1])
                    analysis_dict[i[0]] = list(set((analysis_dict[i[0]])))
        print(analysis_dict)

    if choice == '4':
        shop_items = [
            (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
            (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
            (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
        ]
        print('Тестовые данные добавлены!')

    if choice == '5':
        print(help_description)

