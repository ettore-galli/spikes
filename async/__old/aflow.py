# https://towardsdatascience.com/why-you-should-use-async-in-python-6ab53740077e
# http://zderadicka.eu/functional-fun-with-asyncio-and-monads/

from __future__ import annotations

from typing import Any, Callable, Coroutine, List, Optional
import aiohttp
import asyncio
import copy


async def get_session():
    return aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))


# async def http_get(session: aiohttp.ClientSession, url: str) -> Coroutine:
#     """Execute an GET http call async"""
#     async with session.get(url) as response:
#         resp = await response.json()
#         return resp


async def http_plain_get(session: aiohttp.ClientSession, url: str) -> Coroutine:
    """Execute an GET http call async"""
    async with session.get(url) as response:
        resp = await response.text()
        return resp


# async def http_post(session: aiohttp.ClientSession, url: str) -> Coroutine:
#     """Execute an POST http call async"""
#     async with session.post(url) as response:
#         resp = await response.json()
#         return resp


# async def fetch_all(urls: List, inner: Callable):
#     """Gather many HTTP call made async"""
#     async with aiohttp.ClientSession(
#         connector=aiohttp.TCPConnector(verify_ssl=False)
#     ) as session:
#         tasks = []
#         for url in urls:
#             tasks.append(inner(session, url))
#         responses = await asyncio.gather(*tasks, return_exceptions=True)
#         return responses


# async def longsum(a, b):
#     await asyncio.sleep(2)
#     return a + b


# async def longquare(x):
#     await asyncio.sleep(2)
#     return x**2


# def workflow():
#     print("workflow")
#     work = asyncio.run(longsum(3, 14))
#     print(type(work))
#     print(type(longsum(3, 14)))


async def get_data():
    session = await get_session()
    async with session:
        work = await http_plain_get(session=session, url="http://www.html.it")
        return work


def workflow_2():
    print("workflow 2")
    work = asyncio.run(get_data())
    return work


class AsyncFlow:
    def __init__(
        self,
        result: Optional[Any] = None,
        success: Optional[bool] = None,
        message: Optional[str] = None,
    ) -> None:
        self.result = result
        self.success = success

    @classmethod
    def unit(
        cls,
        result: Optional[Any] = None,
        success: Optional[bool] = None,
        message: Optional[str] = None,
    ):
        return AsyncFlow(result=result, success=success, message=message)

    def bind(self, f: Callable[[Any], AsyncFlow]):
        return f(copy.deepcopy(self.result))


# ___ def run():
#     comments = [
#         f"https://jsonplaceholder.typicode.com/comments/{id_}" for id_ in range(1, 500)
#     ]
#     responses = asyncio.get_event_loop().run_until_complete(
#         fetch_all(comments, http_get)
#     )
#     print(responses)


# run()

if __name__ == "__main__":
    r = workflow_2()
    print(r)
