




import asyncio


async def process():
    print("Hello")
    await asyncio.sleep(1)
    print("world")


if __name__ == '__main__':
    asyncio.run(process(), debug=True)