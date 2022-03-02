from math import pi


class Shape(object):
    def __str__(self):
        return f"Периметр: {self.perimeter()}; Площадь: {self.area()}"

    def perimeter(self):
        return None

    def area(self):
        return None


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):
    def __init__(self, side_size):
        super().__init__(side_size, side_size)


s = Square(3)
print(s)
