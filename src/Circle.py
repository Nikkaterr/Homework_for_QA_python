import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, r, name="Круг"):
        super().__init__(name)
        self.__r = r

    def exist_circle(self):
        if self.__r > 0:
            return True
        else:
            return False

    @property
    def area(self):
        if self.exist_circle() is True:
            return round(math.pi*(self.__r ** 2))
        else:
            return "None"

    @property
    def perimeter(self):
        if self.exist_circle() is True:
            return round(2 * math.pi * self.__r)
        else:
            return "None"

