while True:
    try:
        print("Введите 2 числа")
        a = int(input())
        b = int(input())
        print(a / b)
        lst = [1, 2]
        break
    except (ValueError, EOFError):
        print("Числа введены неверно")
    except ZeroDivisionError:
        print("Делить на 0 нельзя")
    finally:
        print("hi")

