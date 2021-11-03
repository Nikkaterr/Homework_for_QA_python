from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height, name="Прямоугольник"):
        super().__init__(name)
        self.__width = width
        self.__height = height

    def exist_rectangle(self):
        if self.__height > 0 and self.__width > 0:
            return True
        else:
            return False

    @property
    def area(self):
        if self.exist_rectangle() is True:
            return self.__width * self.__height
        else:
            return 'None'

    @property
    def perimeter(self):
        if self.exist_rectangle() is True:
            return self.__width * 2 + self.__height * 2
        else:
            return 'None'
