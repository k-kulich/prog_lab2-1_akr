import asyncio


async def task_first(sleep_a: float = 1, sleep_b: float = 4):
    """Первая корутина: 3 принта с паузами sleep_a и sleep_b."""
    print("Task 1: step 1")
    await asyncio.sleep(sleep_a)
    print("Task 1: step 2")
    await asyncio.sleep(sleep_b)
    print("Task 1: step 3")


async def task_second(sleep_a: float = 3, sleep_b: float = 1, sleep_c: float = 1):
    """Вторая корутина: 4 принта с паузами sleep_a, sleep_b и sleep_c."""
    print("Task 2: step 1")
    await asyncio.sleep(sleep_a)
    print("Task 2: step 2")
    await asyncio.sleep(sleep_b)
    print("Task 2: step 3")
    await asyncio.sleep(sleep_c)
    print("Task 2: step 4")


async def main():
    await asyncio.gather(task_first(), task_second())


if __name__ == '__main__':
    asyncio.run(main())