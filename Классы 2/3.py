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
        self.side = a

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


def print_shape_info(shape):
    print(f"Периметр: {shape.perimeter()}; Площадь: {shape.area()}")


c = Circle(3)
s = Square(3)

print_shape_info(c)
print_shape_info(s)

if isinstance(c, Circle):
    print("Это круг")

