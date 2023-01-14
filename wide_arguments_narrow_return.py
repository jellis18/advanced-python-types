from typing import Iterable, List, Sequence


# Use general types not union
def filter_things(things: Iterable[str], filter_string: str) -> List[str]:
    return [t for t in things if filter_string not in t]


def get_fifth_element(things: Sequence[str]) -> str:
    if len(things) < 5:
        raise ValueError(f"Length of input must be >= 5, found len={len(things)}")
    return things[4]


if __name__ == "__main__":

    # list input is fine
    things = ["badger", "snake", "mushroom"]
    filtered_things = filter_things(things, "mushroom")
    print(f"filter things with list input: {filtered_things}")

    # tuple is good too
    things = ("badger", "snake", "mushroom")
    filtered_things = filter_things(things, "mushroom")
    print(f"filter things with tuple input: {filtered_things}")

    # set, also good
    things = {"badger", "snake", "mushroom"}
    filtered_things = filter_things(things, "mushroom")
    print(f"filter things with set input: {filtered_things}")

    # even generator is good
    things = (t for t in ["badger", "snake", "mushroom"])
    filtered_things = filter_things(things, "mushroom")
    print(f"filter things with generator input: {filtered_things}")

    elements = ("earth", "wind", "water", "fire", "multipass")
    fifth_element = get_fifth_element(elements)
