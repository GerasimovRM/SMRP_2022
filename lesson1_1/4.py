from math import pi


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Square:
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return 4 * self.a


def print_shape_info(shape):
    print(f"Класс: {shape.__class__.__name__}; Периметер: {shape.perimeter()}; Площадь: {shape.area()}")


s = Square(3)
c = Circle(3)
print_shape_info(s)
print_shape_info(c)
if isinstance(c, Circle):
    print("Да, это круг")

