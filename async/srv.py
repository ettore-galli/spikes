import asyncio
import functools
import itertools


async def read_until_data(async_read_callable):
    data = b""
    while True:
        chunk = await async_read_callable()
        print(chunk, len(chunk))
        if len(chunk) < 12:
            break
        data += chunk
    return data


async def serve(reader, writer):
    b_request = await reader.readuntil(b"\r\n")
    b_headers = await reader.readuntil(b"\r\n\r\n")

    b_body = await reader.read(
        1024
    )  # await read_until_data(functools.partial(reader.read, 32))

    request, headers, body = map(str, [b_request, b_headers, b_body])

    print("-" * 50)
    for part in [request, headers, body]:
        print(part)

    writer.write(b"HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n")
    writer.write(b"<!DOCTYPE html><html><body>hello</body></html>")

    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(serve, "0.0.0.0", 8765)

    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:
        print(dir(server))
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
