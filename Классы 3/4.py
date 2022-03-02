import datetime


class Greeter:
    def greet(self):
        print("Good news, everyone!")


class GreeterWithDate(Greeter):
    def greet(self):
        print(datetime.datetime.now())
        super().greet()


g = GreeterWithDate()
g.greet()