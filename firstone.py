import asyncio

async def my_coroutine(n):
    print(f'starting number {n} . . .')
    await asyncio.sleep(2)
    print(f'ending number {n} . . .')

async def main():
    await asyncio.gather(my_coroutine(1), my_coroutine(2), my_coroutine(3))

asyncio.run(main())