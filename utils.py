import time
from typing import TypeVar

T = TypeVar("T")


def pr(value: T, title: str | None = None, r: bool = False) -> T | None:
    if title:
        print(f"+++++++++++++++++ {title} ++++++++++++++++++")
    else:
        print(f"+++++++++++++++++++++++++++++++++++")

    print(type(value))
    display(value)  # type: ignore
    print("-----")
    print("")
    if r:
        return value


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        pr(f"{end_time - start_time} seconds", "Execution time")

    return wrapper
