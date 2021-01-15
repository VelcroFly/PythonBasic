"""Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****."""


class Cell:

    cells_amount: int

    def __init__(self, cells_amount):
        self.cells_amount = cells_amount

    def __str__(self):
        return str(self.cells_amount)

    def __add__(self, other):
        return Cell(self.cells_amount + other.cells_amount)

    def __sub__(self, other):
        if self.cells_amount < other.cells_amount:
            return Cell(other.cells_amount - self.cells_amount)
        else:
            return Cell(self.cells_amount - other.cells_amount)

    def __mul__(self, other):
        return Cell(self.cells_amount * other.cells_amount)

    def __floordiv__(self, other):
        if self.cells_amount < other.cells_amount:
            return Cell(other.cells_amount // self.cells_amount)
        else:
            return Cell(self.cells_amount // other.cells_amount)

    def make_order(self, row):
        result = ['*' * row + '\n' for _ in range(self.cells_amount // row)]
        return ''.join(result) + (self.cells_amount % row) * '*'


if __name__ == '__main__':
    cell_1 = Cell(10)
    cell_2 = Cell(12)
    cell_3 = Cell(20)
    print(cell_1 + cell_2 + cell_3)
    print(cell_1 - cell_2 - cell_3)
    print(cell_1 * cell_2 * cell_3)
    print(cell_1 // cell_2 // cell_3)
    print(cell_2.make_order(5))
    print(cell_2.make_order(15))

