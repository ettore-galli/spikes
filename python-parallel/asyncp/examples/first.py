import asyncio


async def main(who: str):
    print(f"Hello, {who}!")


if __name__ == "__main__":
    asyncio.run(main("world"))
