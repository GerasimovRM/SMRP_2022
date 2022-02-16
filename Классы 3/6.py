class A:
    pass


class K:
    def bar(self):
        print("bar k")


class B(A, K):
    pass


class C(A):
    pass


class E(B):
    pass


class F(C):
    def bar(self):
        print("bar f")

# E->A, F->A, E->K
class G(E, F):
    pass


g = G()
g.bar()

