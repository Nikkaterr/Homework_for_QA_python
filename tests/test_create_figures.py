from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle


# Rectangle

def test_exist_rectangle_valid_value():
    rect1 = Rectangle(10, 20)
    rect1_exist = rect1.exist_rectangle()
    assert rect1_exist is True


def test_exist_rectangle_value_0():  # невалидные значения
    rect2 = Rectangle(0, 200)
    rect2_exist = rect2.exist_rectangle()
    assert rect2_exist is False


def test_exist_rectangle_negative_value():  # невалидные значения
    rect3 = Rectangle(1000, -1)
    rect3_exist = rect3.exist_rectangle()
    assert rect3_exist is False


def test_exist_rectangle_letters():  # невалидные значения
    rect4 = Rectangle("qwert$y", 25)
    rect4_exist = rect4.exist_rectangle()
    assert rect4_exist is False


def test_exist_rectangle_null():  # невалидные значения
    rect5 = Rectangle(7)
    rect5_exist = rect5.exist_rectangle()
    assert rect5_exist is False


# Square


def test_exist_square_valid_value():
    square1 = Square(10)
    square1_exist = square1.exist_square()
    assert square1_exist is True


def test_exist_square_value_0():  # невалидные значения
    square2 = Square(0)
    square2_exist = square2.exist_square()
    assert square2_exist is False


def test_exist_square_negative_value():  # невалидные значения
    square3 = Square(-1)
    square3_exist = square3.exist_square()
    assert square3_exist is False


def test_exist_square_letters():  # невалидные значения
    square4 = Square("6")
    square4_exist = square4.exist_square()
    assert square4_exist is False


def test_exist_square_null():  # невалидные значения
    square5 = Square()
    square5_exist = square5.exist_square()
    assert square5_exist is False

# Circle


def test_exist_circle_valid_value():
    circle1 = Circle(11)
    circle1_exist = circle1.exist_circle()
    assert circle1_exist is True


def test_exist_circle_value_0():  # невалидные значения
    circle2 = Circle(0)
    circle2_exist = circle2.exist_circle()
    assert circle2_exist is False


def test_exist_circle_negative_value():  # невалидные значения
    circle3 = Circle(-1)
    circle3_exist = circle3.exist_circle()
    assert circle3_exist is False


def test_exist_circle_letters():  # невалидные значения
    circle4 = Circle("!@#*")
    circle4_exist = circle4.exist_circle()
    assert circle4_exist is False


def test_exist_circle_null():  # невалидные значения
    circle5 = Circle()
    circle5_exist = circle5.exist_circle()
    assert circle5_exist is False

# Triangle


def test_exist_triangle_valid_value():
    triangle1 = Triangle(11, 12, 13)
    triangle1_exist = triangle1.exist_triangle()
    assert triangle1_exist is True


def test_exist_triangle_ab_less_c():  # невалидные значения
    triangle2 = Triangle(5, 4, 10)
    triangle2_exist = triangle2.exist_triangle()
    assert triangle2_exist is False


def test_exist_triangle_ac_less_b():  # невалидные значения
    triangle3 = Triangle(5, 6, 0)
    triangle3_exist = triangle3.exist_triangle()
    assert triangle3_exist is False


def test_exist_triangle_bc_less_a():  # невалидные значения
    triangle4 = Triangle(25, 1, -1)
    triangle4_exist = triangle4.exist_triangle()
    assert triangle4_exist is False


def test_exist_triangle_letters():  # невалидные значения
    triangle5 = Triangle("qwert$y", 25, 'тест')
    triangle5_exist = triangle5.exist_triangle()
    assert triangle5_exist is False


def test_exist_triangle_null():  # невалидные значения
    triangle6 = Triangle(7, 8)
    triangle6_exist = triangle6.exist_triangle()
    assert triangle6_exist is False

