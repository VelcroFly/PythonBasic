"""Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title}: Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title}: Запуск отрисовки ручкой.')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title}: Запуск отрисовки карандашом.')


class Handle(Stationery):

    def draw(self):
        print(f'{self.title}: Запуск отрисовки маркером.')


if __name__ == '__main__':
    pen = Stationery('Pen')
    pen.draw()

    another_pen = Pen('Another pen')
    another_pen.draw()

    pencil = Pencil('Pencil')
    pencil.draw()

    handle = Handle('Handle')
    handle.draw()
