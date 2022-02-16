class C:
    pass


class A(C):
    def foo(self):
        return "foo2"

    def bar(self):
        return "bar2"


class B(A):
    # расширения метода
    def bar(self):
        upper_bar = super().bar()
        return upper_bar + ' ' + 'bar'

    # переопределение метода
    def foo(self):
        return "foo"



a = A()
print(a.foo())
b = B()
print(b.foo())
print(b.bar())
