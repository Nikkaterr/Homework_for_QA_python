from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle

# Rectangle


def test_area_rectangle():
    rect1 = Rectangle(10, 20)
    rect1_area = rect1.area
    assert rect1_area == 200

# Square


def test_area_square():
    square1 = Square(20)
    square1_area = square1.area
    assert square1_area == 400


# Triangle


def test_area_triangle():
    triangle1 = Triangle(12, 13, 14)
    triangle1_area = triangle1.area
    assert triangle1_area == 72

# Circle


def test_area_circle():
    circle1 = Circle(12)
    circle1_area = circle1.area
    assert circle1_area == 452

