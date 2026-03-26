import ray


@ray.remote
def f(x: int):
    return x * x


if __name__ == "__main__":
    """Initializes Ray Session"""
    ray.init()

    # result = ray.get(f.remote(5))

    results = ray.get([f.remote(i) for i in range(5)])  # result(s)

    print(results)
