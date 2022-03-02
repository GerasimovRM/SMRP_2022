lst = ['123', '23', '214', '124214', '23', '14', '3']
it = list(map(lambda x: int(x) ** 2, lst))
it2 = list(filter(lambda x: x[-1] == '4', lst))
it3 = enumerate(lst, 10)
it4 = list(map(int, filter(lambda x: x[-1] == '4', lst)))

data = ["vabc",  'cca', "bac", 'cab', 'hg']
print(sorted(data, key=lambda x: (len(x), x)))
print(min(data, key=len))

lst2 = [[1, 2], [3, 4], [5, 6]]
lst3 = list(map(lambda x: x[0] + x[1], lst2))
print(lst3)
