import asyncio
import sys

from aiohttp import ClientSession
from asyncp.scraper.file_reader import read_url_list

from asyncp.scraper.file_writer import save_url_list
from asyncp.scraper.notifier import Notifier
from asyncp.scraper.scraper import perform_single_site_scraping

"""
python asyncp/scraper/main.py example-data/urls.txt output/output.txt
"""


async def process_single_site(
    session: ClientSession, output_file: str, url: str, notifier: Notifier
) -> None:
    await notifier.notify(message=f"Scraping {url}")
    scraping_result = await perform_single_site_scraping(
        client_session=session,
        url=url,
    )

    if scraping_result.success:
        await notifier.notify(message=f"Scraping success for {url}")
        await save_url_list(output_file=output_file, url_list=scraping_result.links)
        await notifier.notify(message=f"Links for {url} saved to {output_file}")
    else:
        await notifier.notify(message=f"Failed to download {url}")


async def main(url_list_file: str, output_file: str):
    async with ClientSession() as session:
        processes = [
            process_single_site(
                session=session,
                output_file=output_file,
                url=url,
                notifier=Notifier(),
            )
            for url in await read_url_list(url_list_file)
        ]
        await asyncio.gather(*processes)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
