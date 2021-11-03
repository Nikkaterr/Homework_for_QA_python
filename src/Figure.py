class Figure:
    def __init__(self, name):
        self.name = name

    @property
    def area(self):
        yield

    @property
    def perimeter(self):
        yield

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            return "None"

