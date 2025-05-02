import aiofiles


async def save_url_list(output_file: str, url_list: list[str]) -> None:
    async with aiofiles.open(output_file, "a") as f:
        for url in url_list:
            await f.write(f"{url.strip()}\n")
