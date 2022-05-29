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


async def process_single(session, url):
    async def fetch_data(url) -> str:
        return await http_get(session, url)

    async def save_data(data) -> None:
        return await store_results(data)

    chain = [url, fetch_data, save_data]
    chain.reverse()
    r = await bind_async(*chain)
    return r


async def process_all():
    http_session = await get_session()
    async with http_session as session:
        await process_single(session, WEBSITES[0])


async def bind_async(*args: Callable[[Any], Any]):
    print(args)
    return await args[0](await bind_async(*args[1:])) if len(args) > 1 else args[0]


def workflow():
    asyncio.run(process_all())


if __name__ == "__main__":
    r = workflow()
    # print(r)
