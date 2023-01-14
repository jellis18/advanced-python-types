from typing import Iterable, List, TypeVar, overload

from typing_extensions import reveal_type

Number = TypeVar("Number", int, float)

## TODO: use boto as example here


@overload
def square(value: Number) -> Number:
    ...


@overload
def square(value: Iterable[Number]) -> List[Number]:
    ...


def square(value: Iterable[Number] | Number) -> List[Number] | Number:
    if isinstance(value, (int, float)):
        return value**2
    return [v**2 for v in value]


if __name__ == "__main__":
    s = square([1, 2, 3, 4])
    reveal_type(s)

    s = square(4.5)
    reveal_type(s)

    s = square(1)
    reveal_type(s)
