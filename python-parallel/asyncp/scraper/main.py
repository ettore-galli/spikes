import asyncio
import sys

from aiohttp import ClientSession
from asyncp.scraper.file_reader import read_url_list
from asyncp.scraper.downloader import download_url, look_for_links
from asyncp.scraper.file_writer import save_url_list
from asyncp.scraper.notifier import Notifier

"""
python asyncp/scraper/main.py example-data/urls.txt output/output.txt
"""


async def process_single_site(
    session: ClientSession, output_file: str, url: str, notifier: Notifier
) -> None:
    result = await download_url(session, url)
    if result.success:
        if result.content:
            await notifier.notify(message=f"Retrieving links for {url}")
            await save_url_list(
                output_file=output_file, url_list=look_for_links(result.content)
            )
            await notifier.notify(message=f"Links for {url} saved to {output_file}")
        else:
            await notifier.notify(message=f"Failed to download {url}")


async def main(url_list_file: str, output_file: str):
    async with ClientSession() as session:
        for url in await read_url_list(url_list_file):
            await process_single_site(
                session=session,
                output_file=output_file,
                url=url,
                notifier=Notifier(),
            )


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
