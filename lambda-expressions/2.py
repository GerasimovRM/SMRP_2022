numbers = input().split()
# 1
lst = []
for elem in numbers:
    lst.append(int(elem))
# 2
lst = [int(elem) for elem in numbers]
# 3
lst = list(map(int, numbers))
print(lst)