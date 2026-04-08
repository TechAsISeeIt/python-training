def add(a: int, b: int) -> int:
    return a + b


def get_length(s: str) -> dict[str | int, int | str] | None:
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return {"length": len(s), 1: s}


if __name__ == "__main__":
    print("Sum:", add(1, 2))
    print("Length:", get_length("Hello"))
