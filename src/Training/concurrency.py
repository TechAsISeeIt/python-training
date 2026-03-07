import asyncio
import httpx

urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/uuid",
    "https://httpbin.org/ip",
]


async def fetch(client, url):
    response = await client.get(url)
    print(f"{url} -> {response.status_code}")
    return response


async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for r in results:
            print(r.json())


if __name__ == "__main__":
    asyncio.run(main())
