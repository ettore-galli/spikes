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


async def process_sites(_) -> Iterator[Future[Coroutine]]:
    http_session = await get_session()
    async with http_session as session:
        jobs = asyncio.as_completed(
            [http_get(session=session, url=url) for url in WEBSITES]
        )
        return jobs


async def store_results(result) -> Workflow:
    print("*" * 78)
    print(result[:78])
    print("*" * 78)


async def process_one(session, url):
    # result = await http_get(session, url)
    # await store_results(result)

    async def fetch_data(url) -> Workflow:
        return Workflow(result=await http_get(session, url))

    async def save_data(data) -> Workflow:
        await store_results(data)
        return Workflow(success=True)

    await (await Workflow.unit(result=url).bind(fetch_data)).bind(save_data)


async def process():
    step1 = await process_sites(None)
    print(type(step1))


async def process_all():
    http_session = await get_session()
    async with http_session as session:
        await process_one(session, WEBSITES[0])


def workflow():
    # asyncio.run(AsyncFlow.unit().bind(process_sites).bind(store_results))
    asyncio.run(process_all())


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
        return await f(copy.deepcopy(self.result))


if __name__ == "__main__":
    r = workflow()
    # print(r)
