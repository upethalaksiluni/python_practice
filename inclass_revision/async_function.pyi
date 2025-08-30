import asyncio


async def task1():
    print("Task 1 executed")
    await asyncio.sleep(1)
    print("Task 1 finished")

async def task2():
    print("Task 2 executed")
    await asyncio.sleep(1)
    print("Task 2 finished")


async def main():
    await task1()
    await task2()

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())