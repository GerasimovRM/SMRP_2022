import time
from datetime import datetime


def dish(num, prepare, wait):
    print(f"Время начала подготовки: {datetime.now().strftime('%HH:%MM:%SS')}")
    time.sleep(prepare)
    print(f"Время начала ожидания: {datetime.now().strftime('%HH:%MM:%SS')}")
    time.sleep(wait)
    print(f"Блюдо {num} готово в {datetime.now().strftime('%HH:%MM:%SS')}")


def main():
    dish(1, 2, 3)
    dish(2, 5, 10)
    dish(3, 3, 5)


if __name__ == "__main__":
    t0 = time.time()
    main()
    delta_time = time.time() - t0
    print(f"Время готовки {delta_time}")


