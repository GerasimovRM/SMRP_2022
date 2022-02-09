class Time:
    def __init__(self, m, s):
        self.minutes = m
        self.seconds = s

    def __add__(self, other):
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes
        if seconds >= 60:
            seconds -= 60
            minutes += 1
        return Time(minutes, seconds)

    def __str__(self):
        return f"{self.minutes}:{self.seconds}"

    def __repr__(self):
        return f"Time({self.minutes}, {self.seconds})"  # str(self)


t1 = Time(3, 50)
t2 = Time(4, 20)
t3 = t1 + t2  # t1.__add__(t2)
lst = [t1, t2, t3]
print(t1, t2, t3)
print(lst)