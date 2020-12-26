"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('employees.txt', 'r') as file:
    employees_counter = 0
    overall_salary = 0

    for line in file:
        name, salary = line.split(';')
        employees_counter += 1
        overall_salary += float(salary)
        if float(salary) < 20000:
            print(name)

    print(f'Средняя величина дохода: {(overall_salary / employees_counter):.2f}')
