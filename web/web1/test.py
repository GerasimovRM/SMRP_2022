def func(*args, **kwargs):
    print(*args, **kwargs)


func(1, 2, 3, 4, 5, sep='##', end='<<<\n')