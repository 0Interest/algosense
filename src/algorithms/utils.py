from typing import Any


def swap(array: list[Any], i: int, j: int) -> list[Any]:
    array[i], array[j] = array[j], array[i]
    return array


def merge(array1: list[int], array2: list[int]) -> list[int]:
    merged_array = []
    i, j = 0, 0

    while i != len(array1) or j != len(array2):

        if i == len(array1) or j == len(array2):
            break

        if array1[i] <= array2[j]:
            merged_array.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            merged_array.append(array2[j])
            j += 1

    merged_array.extend(array1[i:])
    merged_array.extend(array2[j:])
    return merged_array
