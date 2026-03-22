import httpx
import asyncio
import json


async def fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/users")
        return response.json()


def write_report(path: str, data: dict[str, str | int]):
    with open(path, "w") as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    result = asyncio.run(fetch())
    write_report("report.json", result)
