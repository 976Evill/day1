# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Room:
    def __init__(self, nazvanie):
        self.nazvanie = nazvanie
        self.wd = []
        self.square = 0

    def add_piggak(self, height):
        self.wd.append(Pidgak(height * 2 + 0.3))

    def add_palto(self, razmer):
        self.wd.append(Palto(razmer / 6.5 + 0.5))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square += el.square
        return main_square


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method_1(self):
        pass

    @abstractmethod
    def my_method_2(self):
        pass


class Pidgak(MyAbstractClass):
    def __init__(self, height):
        self.square = height


    def my_method_1(self):
        print("Пиджак стильный")

    def my_method_2(self):
        print("Отстал от моды")


class Palto(MyAbstractClass):
    def __init__(self, razmer):
        self.square = razmer

    @property
    def my_method(self):
        return f"Добавили в пальто:" \
               f" {self.square}"

    def my_method_1(self):
        print("Вау Суперпальто")

    def my_method_2(self):
        print("Nein? Nicht? NO?")


r = Room('test')
r.add_piggak(125)
r.add_piggak(166)
r.add_piggak(186)
r.add_palto(54)
print("Обший расход % .2f м" % (r.common_square()))
a = Pidgak(100)
a.my_method_2()

b = Palto(180)
b.my_method_2()
print(b.my_method)
