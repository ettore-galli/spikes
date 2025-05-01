from dataclasses import dataclass
import re
from typing import List, Optional
from aiohttp import ClientSession

from asyncp.scraper.base import Issue, IssueType


@dataclass
class DownloadResult:
    url: str
    content: Optional[str]
    success: bool
    issues: List[Issue]


HREF_RE = re.compile(r'href="(.*?)"')


async def download_url(client_session: ClientSession, url: str) -> DownloadResult:
    response = await client_session.get(url)
    success: bool = response.status == 200
    if not success:
        return DownloadResult(
            url=url,
            content=None,
            success=success,
            issues=[
                Issue(
                    message=f"Failed to download {url} ",
                    issue_type=[IssueType.ERROR],
                    data=response.status,
                )
            ],
        )
    text = await response.text()
    return DownloadResult(
        url=url,
        content=text,
        success=success,
        issues=(
            []
            if success
            else [
                Issue(
                    message=f"Failed to download {url} ",
                    issue_type=[IssueType.ERROR],
                    data=response.status,
                )
            ]
        ),
    )


def look_for_links(content: str) -> List[str]:
    return [item for item in HREF_RE.findall(content)]
