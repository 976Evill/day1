# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
import numpy as np


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return f"({self.lists})"

    def __add__(self, other):
        return Matrix(self.lists + other.lists)


a = Matrix(np.matrix('3,2,1;5,6,8'))
print(f"матрица 1 \n {a}")
b = Matrix(np.matrix('13,12,21;15,46,88'))
print(f"матрица 2 \n {b}")
c = a + b
print(f"Сумма матриц: \n {c}")
