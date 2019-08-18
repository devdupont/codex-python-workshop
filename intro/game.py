"""
Dunder method and decorator demo
"""

from functools import wraps
from typing import Any, Callable

# This is an example of a custom decorator.
# A decorator accepts and returns a function


def mydec(f: Callable) -> Callable:
    """
    This decorator adds some print statements around a function call
    """

    # The `wraps` decorators copies the doc strings to the new function
    @wraps(f)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Calling {f} with {args} and {kwargs}")
        resp = f(*args, **kwargs)
        print(f"Done with {resp}")
        return resp

    return wrapper


@mydec
def get_some(how_much: int) -> int:
    return " ! ".join(["LOVE"] * how_much)


class Chest:
    """
    A chest containing gold
    """

    items: [int]
    locked: bool = True

    # Called when creating a new object
    def __init__(self, items: [int] = None):
        # Remeber not to use [] and {} as default values
        if items is None:
            items = []
        self.items = items

    # Called when printing object
    # Similar to __str__
    def __repr__(self) -> str:
        return f"Chest with {self.items}"

    # @property lets us call .value instead of .value()
    @property
    def value(self):
        """
        The value of a chest's contents
        """
        return sum(self.items)

    # Called by len(chest)
    def __len__(self) -> int:
        return len(self.items)

    # Called by + and sum
    def __add__(self, other):
        if not other:
            return sum(self.items)
        return other + sum(self.items)

    # Called by c1 == c2
    def __eq__(self, other) -> bool:
        return other.value == self.value

    # Called by c1 < c2
    def __lt__(self, other) -> bool:
        return self.value < other.value

    # Called by c1 > c2
    def __gt__(self, other) -> bool:
        return self.value > other.value

    # Called when iterating through a chest
    # Ex: for gold in chest:
    def __iter__(self):
        for item in self.items:
            yield item

    # __enter__ and __exit__ are use by the `with` statement
    # Ex: with my_chest as open_chest:

    # __enter__ is called at the start of `with`
    def __enter__(self):
        self.locked = False
        return self

    # __exit__ is called when the `with` indented block exits
    def __exit__(self, *_):
        self.locked = True

    def add_gold(self, value: int):
        """
        Add gold to chest

        Chest must be unlocked first
        """
        if self.locked:
            raise Exception(f"{self} is locked")
        self.items.append(value)


if __name__ == "__main__":

    # Test custom decorator
    print(get_some(5))

    # Create two chests
    better_chest = Chest([1, 2, 3, 4])
    chest = Chest([1, 2])

    # Do two chests contain the same gold
    print(better_chest == chest)

    # Iterate through chest items
    for gold in better_chest:
        print(gold)

    # Add two chests
    print(better_chest + chest)

    # Test Adding multiple chests using sum
    print(sum([better_chest, chest]))

    # Test locking a chest
    print(better_chest)
    with better_chest as chest:
        chest.add_gold(10)
    print(better_chest)
    better_chest.add_gold(1000000000)
    print(better_chest)
