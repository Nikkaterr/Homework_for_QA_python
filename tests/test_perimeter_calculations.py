from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle

# Rectangle


def test_perimeter_rectangle():
    rect1 = Rectangle(10, 20)
    rect1_perimeter = rect1.perimeter
    assert rect1_perimeter == 60

# Square


def test_perimeter_square():
    square1 = Square(20)
    square1_perimeter = square1.perimeter
    assert square1_perimeter == 80


# Triangle


def test_perimeter_triangle():  # валидные значения
    triangle1 = Triangle(12, 13, 14)
    triangle1_perimeter = triangle1.perimeter
    assert triangle1_perimeter == 39

# Circle


def test_perimeter_circle():
    circle1 = Circle(10)
    circle1_perimeter = circle1.perimeter
    assert circle1_perimeter == 63
