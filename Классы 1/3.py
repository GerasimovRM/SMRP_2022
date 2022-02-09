class Car:
    def __init__(self, color="red"):
        self.color = color
        self.__engine_on = False

    def drive_to(self, city):
        if self.__engine_on:
            print(f"Едем в {city}")
        else:
            print("Двигатель не заведен!")

    def key_rotate(self):
        self.__engine_on = not self.__engine_on


c = Car("green")
c.drive_to("Владивосток")
c.key_rotate()
c.drive_to("Владивосток")
c.__engine_on = False
c.drive_to("Владивосток")