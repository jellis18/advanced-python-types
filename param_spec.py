import logging
import time
from typing import Callable, Optional, ParamSpec, TypeVar, overload

from typing_extensions import reveal_type

T = TypeVar("T")
P = ParamSpec("P")


def _default_display_fn(function_name: str, call_time: float) -> None:
    print(f"function: {function_name} ran in {call_time} seconds")


@overload
def timer(__func: Callable[P, T]) -> Callable[P, T]:
    ...


@overload
def timer(*, display_fn: Callable[[str, float], None]) -> Callable[[Callable[P, T]], Callable[P, T]]:
    ...


def timer(
    __func: Optional[Callable[P, T]] = None,
    *,
    display_fn: Optional[Callable[[str, float], None]] = None,
) -> Callable[[Callable[P, T]], Callable[P, T]] | Callable[P, T]:

    display_fn = display_fn or _default_display_fn

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        def inner(*args: P.args, **kwargs: P.kwargs) -> T:
            tstart = time.perf_counter()
            out = func(*args, **kwargs)
            display_fn(func.__name__, time.perf_counter() - tstart)
            return out

        return inner

    if __func is not None:
        return decorator(__func)

    return decorator


def logging_display_fn(function_name: str, call_time: float) -> None:
    logging.info(f"function: {function_name} ran in {call_time} seconds")


@timer(display_fn=logging_display_fn)
def add(a: float, b: float) -> float:
    """
    Add two numbers
    """
    return a + b


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    out = add(3.4, 4.5)
    reveal_type(add)
