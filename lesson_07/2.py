from abc import ABC, abstractmethod

"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""


class Clothes(ABC):

    @abstractmethod
    def materials_expense(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 42:
            self.__v = 42
        elif v > 60:
            self.__v = 60
        else:
            self.__v = v

    def materials_expense(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 100:
            self.__h = 100
        elif h > 220:
            self.__h = 220
        else:
            self.__h = h

    def materials_expense(self):
        return 2 * self.h + 0.3


if __name__ == '__main__':
    coat = Coat(42)
    print(coat.materials_expense())

    another_coat = Coat(15)
    print(another_coat.v)

    costume = Costume(180)
    print(costume.materials_expense())

    another_costume = Costume(500)
    print(another_costume.h)
