class Base1:
    def tic(self):
        print('tic')

    def foo(self):
        print("foo tic")


class Base2:
    def tac(self):
        print('tac')

    def foo(self):
        print("foo tac")


class Derived(Base1, Base2):
    pass


d = Derived()
d.tic()
d.tac()
d.foo()
