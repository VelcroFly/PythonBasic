"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:

    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def get_date(cls, str_date):
        try:
            dd, mm, yyyy = str_date.split('-')
        except ValueError:
            print('Некорректный формат исходных данных!')
        else:
            return dd, mm, yyyy

    @staticmethod
    def validate_date(str_date):
        try:
            dd, mm, yyyy = str_date.split('-')
        except ValueError:
            print(f'{str_date} Некорректный формат исходных данных!')
        else:
            if not 0 < int(mm) < 13:
                return f'{str_date} Недопустимое значение параметра "Месяц"'
            if int(mm) in [1, 3, 5, 7, 8, 10, 12] and not 0 < int(dd) < 32:
                return f'{str_date} Недопустимое значение параметра "День"'
            elif int(mm) in [4, 6, 9, 11] and not 0 < int(dd) < 31:
                return f'{str_date} Недопустимое значение параметра "День"'
            elif int(yyyy) % 4 == 0 and not 0 < int(dd) < 30:
                return f'{str_date} Недопустимое значение параметра "День"'
            elif int(yyyy) % 4 != 0 and not 0 < int(dd) < 29:
                return f'{str_date} Недопустимое значение параметра "День"'
            else:
                return f'{str_date} Заданная дата корректна'

    @staticmethod
    def show_date(obj):
        return f'{obj.dd:02}.{obj.mm:02}.{obj.yyyy:04}'


if __name__ == '__main__':
    date = Date('17-05-1988')
    print(date.get_date('17-05-1988'))

    print(Date.validate_date('17-05-1988'))
    print(Date.validate_date('30-02-1988'))
    print(Date.validate_date('29-02-2019'))
    print(Date.validate_date('29-02-2020'))
    print(Date.validate_date('32-01-2020'))
    print(Date.validate_date('31-04-2020'))
    print(Date.validate_date('31-13-2020'))
