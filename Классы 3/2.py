class A:
    def foo(self):
        print("foo")

    def bar(self):
        print("bar2")


class B(A):
    def bar(self):
        print('bar')


a = A()
a.foo()

b = B()
b.bar()
b.foo()

