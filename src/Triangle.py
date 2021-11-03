from math import sqrt

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c, name="Треугольник"):
        super().__init__(name)
        self.__a = a
        self.__b = b
        self.__c = c

    def exist_triangle(self):
        if self.__a + self.__b > self.__c and self.__a + self.__c > self.__b and self.__c + self.__b > self.__a:
            return True
        else:
            return False

    @property
    def perimeter(self):
        if self.exist_triangle() is True:
            return self.__a + self.__b + self.__c
        else:
            return 'None'

    @property
    def area(self):
        if self.exist_triangle() is True:
            p = self.perimeter / 2
            return round(sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c)))
        else:
            return 'None'
