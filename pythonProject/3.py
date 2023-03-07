s = set()
s.add(3)
s.add(10)
print(s)
s.remove(10)
print(s)

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection_update(b), a)