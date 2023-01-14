from typing import Callable, Sequence, TypeVar

from typing_extensions import reveal_type

T = TypeVar("T", int, float, str, bool)
Array = Sequence[Sequence[T]]

ArrayTransformerFunction = Callable[[Array[T]], Array[T]]


class TransformerPipeline:
    def __init__(self, transformers: Sequence[ArrayTransformerFunction[T]]):
        self._transformers = transformers

    def transform(self, array: Array[T]) -> Array[T]:
        for tfm in self._transformers:
            array = tfm(array)
        return array


def transform1(array: Array[T]) -> Array[T]:
    return array


def transform2(array: Array[T]) -> Array[T]:
    return array


if __name__ == "__main__":
    array = [[1, 2, 3], [4, 5, 6]]

    pipeline = TransformerPipeline([transform1, transform2])

    transformed_array = pipeline.transform(array)
    reveal_type(transformed_array)
