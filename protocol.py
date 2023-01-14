import abc
from typing import Any, Iterable, Protocol, TypeVar

T = TypeVar("T", covariant=True)


class MySequence(Protocol[T]):
    def __getitem__(self, __idx: Any) -> T:
        ...

    def __len__(self) -> int:
        ...


class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self) -> None:
        pass

    @abc.abstractmethod
    def act(self) -> None:
        pass

    @property
    @abc.abstractmethod
    def num_legs(self) -> int:
        pass


class Dog(Animal):
    def make_sound(self) -> None:
        print("woof")

    def act(self) -> None:
        print("dog is walking")

    @property
    def num_legs(self) -> int:
        return 4


class Fish(Animal):
    def make_sound(self) -> None:
        print("blub")

    def act(self) -> None:
        print("fish is swimming")

    @property
    def num_legs(self) -> int:
        return 0


class Fox:
    def make_sound(self) -> None:
        print("?????")


class CanMakeSound(Protocol):
    def make_sound(self) -> None:
        ...


def get_animal_sounds(animals: Iterable[Animal]) -> None:
    for animal in animals:
        animal.make_sound()


def get_animal_sounds_protocol(animals: Iterable[CanMakeSound]) -> None:
    for animal in animals:
        animal.make_sound()


def get_fifth_element(things: MySequence[str]) -> str:
    if len(things) < 5:
        raise ValueError(f"Length of input must be >= 5, found len={len(things)}")
    return things[4]


if __name__ == "__main__":
    # this will raise type error
    elements = {"earth", "wind", "water", "fire", "multipass"}
    fifth_element = get_fifth_element(elements)

    elements = ("earth", "wind", "water", "fire", "multipass")
    fifth_element = get_fifth_element(elements)

    elements = {0: "earth", 1: "wind", 2: "water", 3: "fire", 4: "multipass"}
    fifth_element = get_fifth_element(elements)

    animals = [Dog(), Fish(), Fox()]
    get_animal_sounds(animals)

    get_animal_sounds_protocol(animals)
