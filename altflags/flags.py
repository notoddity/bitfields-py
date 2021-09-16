from typing import Callable, Optional

def _getter(n: int) -> Callable:
    def wrapper(self):
        return self._get(n)
    return wrapper

def _setter(n: int) -> Callable:
    def wrapper(self, b):
        self._set(n, b)
    return wrapper

def flag(n: int) -> property:
    """
    Add new flag to extented Flags class

    Args:
        n (int): Bit position of flag

    Returns:
        property: Builtin python property object
    """
    return property(_getter(n), _setter(n))

class Flags(object):
    """Flags parent class"""
    __slots__ = ("flags")

    def __init__(self, flags: Optional[int] = 0) -> None:
        """
        __init__ Flags class initialization method

        Args:
            flags (Optional[int], optional): Parse passed flags into current model. Defaults to 0.
        """
        self.flags = flags

    def __eq__(self, o: object) -> bool:
        if "flags" in o.__slots__ and o.flags == self.flags:
            return True
        return False

    def _get(self, n: int) -> bool:
        return bool(self.flags >> n & 1)

    def _set(self, n: int, b: bool):
        self.flags = 1 << n | self.flags if b else ~ (1 << n) & self.flags