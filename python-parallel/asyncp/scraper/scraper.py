from dataclasses import dataclass
from aiohttp import ClientSession

from asyncp.scraper.downloader import download_url, look_for_links


@dataclass
class ScrapingResult:
    url: str
    success: bool
    links: list[str]


async def perform_single_site_scraping(
    client_session: ClientSession,
    url: str,
) -> ScrapingResult:
    download_result = await download_url(client_session, url)
    if download_result.success and download_result.content:
        return ScrapingResult(
            url=url, success=True, links=look_for_links(download_result.content)
        )
    else:
        return ScrapingResult(
            url=url,
            success=False,
            links=[],
        )
