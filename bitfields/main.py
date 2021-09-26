from typing import Callable, Union

class Fields():

    def __init__(self, value: int = 0) -> None:
        self.value = value

    def __int__(self) -> int:
        return int(self.value)
    
    def __str__(self) -> str:
        return str(self.value)

    def __get(self, n: int) -> bool:
        return bool(self.value >> n & 1)
    
    def _getter(n: int) -> Callable:
        def inner(self):
            return self.__get(n)
        return inner

    def __set(self, n: int, b: Union[bool, int]) -> None:
        self.value = 1 << n | self.value if b else ~ (1 << n) & self.value
    
    def _setter(n: int) -> Callable:
        def inner(self, b):
            self.__set(n, b)
        return inner

def field(n: int) -> property:
    return property(Fields._getter(n), Fields._setter(n))