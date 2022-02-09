class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def increment_age(self):
        self.age += 1


p1 = Person("Имя")
p2 = Person("Челик", 23)
print(p1.name, p1.age)
print(p2.name, p2.age)
p2.increment_age()
print(p2.name, p2.age)
