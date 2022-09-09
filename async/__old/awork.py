import asyncio


async def print_delayed(message: str, delay: int = 1):
    await asyncio.sleep(delay)
    print(message)
    return f"Result of {message}"


async def amain():
    tasks = [asyncio.create_task(print_delayed(f"task-{i}", 4)) for i in range(4)]
    print(await asyncio.gather(*tasks, return_exceptions=True))


if __name__ == "__main__":
    asyncio.run(amain())
