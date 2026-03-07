import asyncio


async def greet(name: str) -> None:
    await asyncio.sleep(5)
    print(f"Hello, {name}!")


if __name__ == "__main__":
    asyncio.run(greet("Alice"))
    print("Alice has been greeted.")
