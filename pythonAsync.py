from asyncio import create_task
from asyncio import run
from asyncio import sleep


def runAsync(function):
    return create_task(function)


async def count(value: int) -> None:
    await sleep(value)
    print("time waited: ", value)


async def main():
    runAsync(count(2))
    runAsync(count(4))
    runAsync(count(5))
    await sleep(6)

run(main())
