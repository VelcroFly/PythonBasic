import json
"""Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""

with open('firms.txt', 'r') as file:
    overall_profit = 0
    firm_counter = 0
    firms_list = list()
    firms_dict = dict()
    average_profit_dict = dict()

    for line in file:
        firm_name, firm_type, firm_gain, firm_expense = line.split()
        firm_profit = float(firm_gain) - float(firm_expense)

        if firm_profit > 0:
            overall_profit += firm_profit
            firm_counter += 1
        firms_dict[firm_name] = firm_profit

    firms_list.append(firms_dict)

    average_profit = overall_profit / firm_counter
    average_profit_dict['average_profit'] = round(average_profit, 2)
    firms_list.append(average_profit_dict)

    with open('7 res.txt', 'w') as res_file:
        res_file.write(json.dumps(firms_list))
