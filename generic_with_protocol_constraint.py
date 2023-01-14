from dataclasses import dataclass
from typing import Callable, Protocol, TypeVar, overload

from typing_extensions import Self


class HasLessThan(Protocol):
    def __lt__(self, __other: Self) -> bool:
        ...


T = TypeVar("T", bound=HasLessThan)
S = TypeVar("S")


def _default_key(__val):  # type: ignore
    return __val  # type: ignore


@overload
def max(a: T, b: T) -> T:
    ...


@overload
def max(a: S, b: S, *, key: Callable[[S], T]) -> S:
    ...


def max(a, b, *, key=None):  # type: ignore
    key_func = key or _default_key  # type: ignore
    if key_func(a) < key_func(b):  # type: ignore
        return b  # type:ignore
    return a  # type: ignore


@dataclass
class Line:
    x_min: float
    x_max: float

    def __lt__(self, other: Self) -> bool:
        return (self.x_max - self.x_min) < (other.x_max - other.x_min)


@dataclass
class PlainLine:
    x_min: float
    x_max: float


if __name__ == "__main__":
    m = max(3, 4)
    print(max(3, 4))
    print(max("hello", "world!"))
    print(max(4.5, 3.4))
    print(max([4, 5, 6], [1, 2]))
    print(max(Line(0, 3), Line(0, 5)))
    print(max(PlainLine(0, 3), PlainLine(0, 5), key=lambda line: (line.x_max - line.x_min)))
