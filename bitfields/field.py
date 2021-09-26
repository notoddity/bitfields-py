from typing import Callable

def _getter(n: int) -> Callable:
    def wrapper(self):
        return self._get(n)
    return wrapper

def _setter(n: int) -> Callable:
    def wrapper(self, b):
        self._set(n, b)
    return wrapper

def field(n: int) -> property:
    """
    Add new flag to extented Flags class

    Args:
        n (int): Bit position of flag

    Returns:
        property: Builtin python property object
    """
    return property(_getter(n), _setter(n))