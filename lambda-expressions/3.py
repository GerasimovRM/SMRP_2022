lst = [1, 2, 10, 3]
result = list(map(lambda x: x ** 2, lst))
result1 = list(filter(lambda x: x % 2 == 0, result))
for i, elem in enumerate(result):
    print(i, elem)