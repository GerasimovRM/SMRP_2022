import time
from datetime import datetime
import asyncio


async def dish(num, prepare, wait):
    print(f"Время начала подготовки {num}: {datetime.now().strftime('%HH:%MM:%SS')}")
    await asyncio.sleep(prepare)
    print(f"Время начала ожидания {num}: {datetime.now().strftime('%HH:%MM:%SS')}")
    await asyncio.sleep(wait)
    print(f"Блюдо {num} готово в {datetime.now().strftime('%HH:%MM:%SS')}")


async def main():
    tasks = [asyncio.create_task(dish(1, 2, 3)),
             asyncio.create_task(dish(2, 5, 10)),
             asyncio.create_task(dish(3, 3, 5))]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    t0 = time.time()
    asyncio.run(main())
    delta_time = time.time() - t0
    print(f"Время готовки {delta_time}")


