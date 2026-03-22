import asyncio
import httpx
from datetime import datetime

urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/uuid",
    "https://httpbin.org/ip",
]


async def fetch(client: httpx.AsyncClient, url: str) -> httpx.Response:
    response = await client.get(url)
    print(f"{url} -> {response.status_code}")
    return response


async def normal():
    print(datetime.now())
    async with httpx.AsyncClient() as client:
        for url in urls:
            print(await fetch(client, url))
    print(datetime.now())


async def main():
    print(datetime.now())
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in urls]
        results = await asyncio.gather(*tasks)  # Registering ASync Tasks
        print(results)
    print(datetime.now())


if __name__ == "__main__":
    asyncio.run(normal())
