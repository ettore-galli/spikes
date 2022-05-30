# https://towardsdatascience.com/why-you-should-use-async-in-python-6ab53740077e
# http://zderadicka.eu/functional-fun-with-asyncio-and-monads/

from __future__ import annotations
from concurrent.futures import Future
from sre_constants import SUCCESS

from typing import Any, Callable, Coroutine, Iterator, List, Optional
import aiohttp
import asyncio
import copy


WEBSITES = ["http://www.html.it", "http://www.arcocer.it", "http://www.arcimm.it"]


async def get_session():
    return aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))


async def http_get(session: aiohttp.ClientSession, url: str) -> Coroutine:
    async with session.get(url) as response:
        resp = await response.text()
        return resp


async def store_results(result):
    print("*" * 78)
    print(result[:78])
    print("*" * 78)


# --------------------------------------------------------------------------------


class Workflow:
    def __init__(
        self,
        result: Optional[Any] = None,
        success: Optional[bool] = None,
        message: Optional[str] = None,
    ) -> None:
        self.result = result
        self.success = success
        self.message = message

    @classmethod
    def unit(
        cls,
        result: Optional[Any] = None,
        success: Optional[bool] = None,
        message: Optional[str] = None,
    ):
        return Workflow(result=result, success=success, message=message)

    async def bind(self, f: Callable[[Any], Workflow]):
        async def _step(f: Callable[[Any], Workflow]):
            return f(await self.result)

        return Workflow(result=_step(f))


async def process_one(session, url):
    async def fetch_data(url) -> Workflow:
        return Workflow(result=await http_get(session, url))

    async def save_data(data) -> Workflow:
        return Workflow(result=await store_results(data))

    return await Workflow.unit(url).bind(fetch_data).bind(save_data)


# --------------------------------------------------------------------------------


async def process_single(session, url):
    async def fetch_data(url) -> str:
        return await http_get(session, url)

    async def save_data(data) -> None:
        return await store_results(data)

    chain = [url, fetch_data, save_data]
    r = await bind_async(*chain[::-1])
    return r


async def bind_async(*args: Callable[[Any], Any]):
    return await args[0](await bind_async(*args[1:])) if len(args) > 1 else args[0]


# --------------------------------------------------------------------------------


async def process_all():
    http_session = await get_session()
    async with http_session as session:
        # await process_single(session, WEBSITES[0])
        await process_one(session, WEBSITES[0])


def workflow():
    asyncio.run(process_all())


if __name__ == "__main__":
    r = workflow()
    # print(r)
