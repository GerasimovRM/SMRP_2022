a = (1, 2, 3, 3, 4, 5, 6, 7, 1, 2,3,45, 65)
print(a[0], a[-1])
for elem in a:
    print(elem)

st = "askdfgbiwugoqhaskbdqbh"
print(st[2:])
print(st[:2])
print(st[-4:])
print(st[:-4])
print(st[2:5])
print(st[:10:2])
print(st[::-1])

a, b = 7, 3
a = (1, "2", 3.5)
b = (1, "abc", 3)
print(a > b)