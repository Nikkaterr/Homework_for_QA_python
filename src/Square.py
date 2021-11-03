from src.Figure import Figure


class Square(Figure):
    def __init__(self, width, name="Квадрат"):
        super().__init__(name)
        self.__width = width

    def exist_square(self):
        if self.__width > 0:
            return True
        else:
            return False

    @property
    def area(self):
        if self.exist_square() is True:
            return self.__width ** 2
        else:
            return 'None'

    @property
    def perimeter(self):
        if self.exist_square() is True:
            return self.__width * 4
        else:
            return 'None'
