from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle

# Rectangle


def test_function_from_rectangle():
    rect1 = Rectangle(5, 20)
    triangle1 = Triangle(12, 13, 14)
    sum_area_figures = rect1.add_area(triangle1)
    assert sum_area_figures == 172

# Square


def test_function_from_square():
    square1 = Square(20)
    circle1 = Circle(12)
    sum_area_figures = square1.add_area(circle1)
    assert sum_area_figures == 852


# Triangle


def test_function_from_triangle():  # валидные значения
    triangle1 = Triangle(12, 13, 14)
    circle1 = Circle(12)
    sum_area_figures = triangle1.add_area(circle1)
    assert sum_area_figures == 524

# Circle


def test_function_from_circle():
    circle1 = Circle(10)
    rect1 = Rectangle(5, 20)
    sum_area_figures = circle1.add_area(rect1)
    assert sum_area_figures == 414

# not subclass Figure


def test_function_not_subclass():
    class Animal:
        pass
    dog = Animal()
    rect1 = Rectangle(5, 20)
    sum_area_figures = rect1.add_area(dog)
    assert sum_area_figures == "None"

