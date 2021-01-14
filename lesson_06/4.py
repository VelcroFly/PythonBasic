"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.is_police = is_police
        self.color = color
        self.speed = speed

    def start_moving(self):
        print(f'{self.name} is start moving!')

    def stop_moving(self):
        print(f'{self.name} is stop moving!')

    def turn(self, direction):
        print(f'{self.name} is turning to {direction}!')

    def show_speed(self):
        print(f'Current speed is {self.speed}')


class TownCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print('Warning! High speed!')
        else:
            super().show_speed()


class SportCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=False)


class WorkCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print('Warning! High speed!')
        else:
            super().show_speed()


class PoliceCar(Car):

    def __init__(self, name, speed):
        super().__init__(name, 'police_colors', speed, is_police=True)


if __name__ == '__main__':
    car = Car(name='BMW', color='silver', speed=80, is_police=False)
    car.start_moving()
    car.stop_moving()
    car.turn('left')
    car.show_speed()
    print(car.name, end='\n\n')

    town_car = TownCar('Mazda', 'red', 70)
    print(town_car.name)
    town_car.start_moving()
    town_car.stop_moving()
    town_car.turn('left')
    town_car.show_speed()
    print(town_car.is_police)
    print(town_car.name, end='\n\n')

    work_car = WorkCar('Gazelle', 'White', 50)
    print(work_car.name)
    work_car.show_speed()
    print(work_car.is_police)
    work_car.start_moving()
    print(work_car.name, end='\n\n')

    police_car = PoliceCar('Ford', 90)
    print(police_car.name)
    print(police_car.is_police)
    print(police_car.color)
    print(police_car.name, end='\n\n')
