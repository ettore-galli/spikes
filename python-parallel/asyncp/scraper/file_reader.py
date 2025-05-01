import aiofiles


async def read_url_list(url_list_file: str) -> list[str]:
    async with aiofiles.open(url_list_file, "r") as f:
        urls = [line.strip() for line in await f.readlines()]
    return urls
