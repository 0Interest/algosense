from typing import Any


def swap(array: list[Any, ...], i: int, j: int) -> list[Any, ...]:
    array[i], array[j] = array[j], array[i]
    return array
