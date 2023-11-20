from time import sleep
import asyncio


async def my_co(n):
    print(f'salam{n}')
    await asyncio.sleep(2)
    print(f'bye {n}')

async def main():
    await asyncio.gather(my_co(1))
    sleep(5)
    await asyncio.gather(my_co(2))

asyncio.run(main())

