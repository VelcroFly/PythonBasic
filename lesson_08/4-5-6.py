from abc import ABC, abstractmethod

"""4: Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""

"""5: Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь."""

"""6: Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""


class Warehouse:

    def __init__(self, location):
        self.location = location
        self.oe_count = {
            'Принтер': 0,
            'Сканнер': 0,
            'МФУ': 0
        }

    def receive(self, oe_unit):
        oe_unit.location = 'На складе'
        self.oe_count[oe_unit.oe_type] += 1
        return f'{oe_unit.oe_type} {oe_unit.manufacturer} приехал на склад.'

    def give_out(self, oe_unit, new_location):
        self.oe_count[oe_unit.oe_type] -= 1
        oe_unit.location = new_location
        return f'{oe_unit.oe_type} {oe_unit.manufacturer} отправился в {new_location}'


class OfficeEquipment(ABC):

    def __init__(self, oe_type, manufacturer):
        self.types_dict = {
            1: 'Принтер',
            2: 'Сканнер',
            3: 'МФУ'
        }
        try:
            self.oe_type = self.types_dict[oe_type]
        except KeyError:
            print('Задан некорректный тип оргтехники')
        self.manufacturer = manufacturer
        self.location = str()

    @abstractmethod
    def do_job(self):
        pass

    def __str__(self):
        return f'Информация об устройстве: {self.oe_type} {self.manufacturer}.'


class Printer(OfficeEquipment):

    def do_job(self):
        return f'{self.oe_type} {self.manufacturer} печатает.'


class Scanner(OfficeEquipment):

    def do_job(self):
        return f'{self.oe_type} {self.manufacturer} сканирует.'


class MFU(OfficeEquipment):

    def do_job(self):
        return f'{self.oe_type} {self.manufacturer} сканирует и печает.'


if __name__ == '__main__':
    warehouse = Warehouse('г. Москва, ул. Пушкина')

    printer = Printer(1, 'Epson')
    print(warehouse.receive(printer))
    print(warehouse.receive(printer))
    print(warehouse.oe_count['Принтер'])
