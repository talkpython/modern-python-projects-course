import httpx


async def get_status(url: str) -> int:
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.head(url, allow_redirects=False)
            return resp.status_code
        except (httpx.ConnectError, httpx.UnsupportedProtocol):
            # Probably the URL was wrong
            return 0
        except httpx.ReadTimeout:
            # Timeout
            return -1
