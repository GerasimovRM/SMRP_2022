def logged(func):
    count = 0

    def new_func(*args, **kwargs):
        nonlocal count
        count += 1
        print(count, ">> Arguments:", args, "Names arguments:", kwargs)
        result = func(*args, **kwargs)
        print("-- Result:", result)
        return result

    return new_func


def func(*args, **kwargs):
    print(*args, kwargs)


@logged
def func2(x):
    return x ** 2


func("123", "dds", "asda", a=3, b=123)
print(func2(13))

print(func2(3))
