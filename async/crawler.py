# https://towardsdatascience.com/why-you-should-use-async-in-python-6ab53740077e
# http://zderadicka.eu/functional-fun-with-asyncio-and-monads/

from __future__ import annotations

from typing import Any, Callable, Coroutine, List, Optional
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


async def crawl_sites():
    http_session = await get_session()
    async with http_session as session:
        for job in asyncio.as_completed(
            [http_get(session=session, url=url) for url in WEBSITES]
        ):
            data = await job
            print(job, data[:50])


def workflow():
    asyncio.run(crawl_sites())


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


if __name__ == "__main__":
    r = workflow()
    print(r)
