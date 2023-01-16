import asyncio

async def foo1(mode: str):
    print(mode)

    async def foo2():
        print(mode)

    await foo2()


asyncio.run(foo1("test1"))
asyncio.run(foo1("test2"))
