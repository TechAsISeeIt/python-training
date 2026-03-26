def add(a: int, b: int) -> int:
    return a + b


def get_length(s: str) -> dict[str | int, int | str] | None:
    try:
        if not s:
            raise ValueError("Input must be a string")
        return {"length": len(s), 1: s}
    except ValueError as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    print("Sum:", add(1, 2))
    print("Length:", get_length("Hello"))
