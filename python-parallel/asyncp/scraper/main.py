import asyncio
import sys

from aiohttp import ClientSession
from asyncp.scraper.file_reader import read_url_list
from asyncp.scraper.downloader import download_url, look_for_links

"""
python asyncp/scraper/main.py example-data/urls.txt output/output.txt
"""


async def main(url_list_file: str, output_file: str):

    async with ClientSession() as session:
        for url in await read_url_list(url_list_file):
            result = await download_url(session, url)
            if result.success:
                print(f"Downloaded {url} successfully.")

                with open(output_file, "a") as f:
                    f.write(f"\n{'*'*30} URL: {url} {'*'*30}\n")
                    if result.content:
                        for url in look_for_links(result.content):
                            f.write(f"{url}\n")

            else:
                print(f"Failed to download {url}: {result.issues}")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
