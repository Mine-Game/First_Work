# Создать класс TrafficLight ( светофор) и определить у него один атрибут color ( цвет) и метод
# running ( запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# import time
# import msvcrt
#
# class TrafficLight:
#     # Атрибуты класса
#     __color = ""
#
#     # Методы класса
#     def running(self):
#         quite = None
#         while quite != "q":
#             TrafficLight.__color = "Red"
#             print(TrafficLight.__color)
#             time.sleep(7)
#             TrafficLight.__color = "Yellow"
#             print(TrafficLight.__color)
#             time.sleep(2)
#             TrafficLight.__color = "Green"
#             print(TrafficLight.__color)
#             time.sleep(7)
#             TrafficLight.__color = "Yellow"
#             print(TrafficLight.__color)
#             time.sleep(2)
#             quite = input("Нажмите 'q' для выхода или 'Enter' для продолжения: ").lower()
#
# TrafficLight_1 = TrafficLight()
# TrafficLight_1.running()
############################################################################################
# Реализовать класс Road ( дорога), в котором определить атрибуты: l ength ( длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
# 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
# class Road:
#     # Атрибуты класса
#     def __init__(self, length, width):
#         self._l = length
#         self._w = width
#
#     def AllMass(self, mass, sm):
#         return self._l * self._w * mass * sm
#
#
# length_1 = float(input("Введите длину дороги(м): "))
# width_1 = float(input("Введите ширину дороги(м): "))
# mass_1 = float(input("Введите массу 1 кв метра асфальта(кг): "))
# sm_1 = float(input("Введите толщину асфальта(см): "))
#
# Road_1 = Road(length_1, width_1)
# print(f"Масса: {(Road_1.AllMass(mass_1, sm_1))/1000}т.")
##############################################################################
# Реализовать базовый класс Worker ( работник), в котором определить атрибуты: name,
# surname, position ( должность), i ncome ( доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
# дохода с учетом премии ( get_total_income) . Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).
#
# class Worker:
#     # Атрибуты класса
#     def __init__(self, name, surname, position, income):
#         self.n = name
#         self.s = surname
#         self.p = position
#         self.__i = income
#
#
# class Position(Worker):
#     def worker_method(self):
#         get_full_name = f"Фамилия и Имя сотрудника: {self.n} {self.s} \nДолжность: {self.p}"
#         print(get_full_name)
#         get_total_income = income_1.get("wage") + income_1.get("bonus")
#         print(f"Заработная плата с учётом премии: {get_total_income}")
#
# name_1 = "Andrey"
# surname_1 = "Petrov"
# position_1 = "Developer"
# income_1 = {"wage": 50000, 'bonus': 27000}
#
# Worker_1 = Worker(name_1, surname_1, position_1, income_1)
# Position_1 = Position(name_1, surname_1, position_1, income_1)
# Position_1.worker_method()
#########################################################################
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, i s_police ( булево). А также методы: go, stop, t urn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# ( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
#
#
# class Car:
#     # Атрибуты класса
#     def __init__(self, speed, color, name, is_police=False):
#         self.s = speed
#         self.c = color
#         self.n = name
#         self.i = is_police
#         print(f'Новая машина: {self.n} (цвет {self.c}) машина полицейская - {self.i}')
#
#     def go(self):
#         print(f'{self.n}: Машина поехала')
#
#     def stop(self):
#         print(f'{self.n}: Машина остановилась')
#
#     def turn(self, direction):
#         print(f'{self.n}: Машина повернула {"налево" if direction == 0 else "направо"}.')
#
#     def show_speed(self):
#         print(f"{self.n}: Скорость автомобиля {self.s}")
#
#
# class TownCar(Car):
#     """Городской автомобиль"""
#
#     def show_speed(self):
#         if self.s > 60:
#             print(f"{self.n}: Скорость автомобиля {self.s}, вы превысили допустимый режим в 60, пожалуйста снизьте скорость")
#         else:
#             print(f"{self.n}: Скорость автомобиля {self.s}")
#
#
# class SportCar(Car):
#     """Спортивный автомобиль"""
#
#
# class WorkCar(Car):
#     """Рабочий автомобиль"""
#
#     def show_speed(self):
#         if self.s > 40:
#             print(f"{self.n}: Скорость автомобиля {self.s}, вы превысили допустимый режим в 40, пожалуйста снизьте скорость")
#         else:
#             print(f"{self.n}: Скорость автомобиля {self.s}")
#         return
#
#
# class PoliceCar(Car):
#     """Полицейский автомобиль"""
#
#     def __init__(self, speed, color, name, is_police=True):
#         super().__init__(speed, color, name, is_police)
#
#
# police_car = PoliceCar(80, 'белый', 'Полицейский автомобиль')
# police_car.go()
# police_car.show_speed()
# police_car.turn(0)
# police_car.stop()
#
# print("-"*50)
#
# Town_Car = TownCar(60, 'Зеленый', 'Фордик')
# Town_Car.go()
# Town_Car.show_speed()
# Town_Car.turn(1)
# Town_Car.stop()
#
# print("-"*50)
#
# Sport_Car = SportCar(180, 'Черный', 'Зверюга')
# Sport_Car.go()
# Sport_Car.show_speed()
# Sport_Car.turn(0)
# Sport_Car.stop()
#
# print("-"*50)
#
# Work_Car = WorkCar(90, 'Красный', 'Доходяга')
# Work_Car.go()
# Work_Car.show_speed()
# Work_Car.turn(1)
# Work_Car.stop()
# #################################################################################
# # Реализовать класс Stationery ( канцелярская принадлежность). Определить в нем атрибут title
# # (название) и метод draw ( отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# # три дочерних класса Pen ( ручка), Pencil ( карандаш), Handle ( маркер). В каждом из классов
# # реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# # уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# # метод для каждого экземпляра.
# class Stationery:
#     # Атрибуты класса
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print(f'Запуск отрисовки.')
#
#
# class Pen(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки ручкой "{self.title}".')
#
#
# class Pencil(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки карандашом "{self.title}".')
#
#
# class Handle(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки маркером "{self.title}".')
#
# pen_s = Pen('Ручка-Самобранка')
# pen_s.draw()
#
# pencil_s = Pencil('КарандашЛенд')
# pencil_s.draw()
#
# handle_s = Handle('МаркерСтойкий')
# handle_s.draw()