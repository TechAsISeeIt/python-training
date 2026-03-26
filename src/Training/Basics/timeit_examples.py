import timeit
import time


def add(num: int) -> int:
    result: int = 0
    time.sleep(1)
    for arg in range(num):
        result += arg
    return result


if __name__ == "__main__":
    execution_time = timeit.timeit(lambda: add(1000), number=10)
    print(f"Execution time: {execution_time}")
    etime = timeit.timeit("sum(range(1000))", number=100)
    print(f"Execution time: {etime}")
