import time
"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт."""


class TextColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def change_color(self, new_color):
        if new_color == 'Red':
            self.__color = new_color
            print(f'{TextColors.RED}{self.__color} color phase{TextColors.RED}')
        if new_color == 'Yellow':
            self.__color = new_color
            print(f'{TextColors.YELLOW}{self.__color} color phase{TextColors.YELLOW}')
        if new_color == 'Green':
            self.__color = new_color
            print(f'{TextColors.GREEN}{self.__color} color phase{TextColors.GREEN}')

    def running(self):
        self.change_color('Red')
        time.sleep(7)
        self.change_color('Yellow')
        time.sleep(2)
        self.change_color('Green')
        time.sleep(7)

    def main_cycle(self):
        while True:
            self.running()


if __name__ == '__main__':
    traffic_light = TrafficLight('Red')
    traffic_light.main_cycle()
