from algorithms.utils import swap, merge


def bubble_sort(array: list[int]) -> list[int]:
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i, -1):
            if array[i] > array[j]:
                swap(array, i, j)
    return array


def merge_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_array = merge_sort(array[: middle])
    right_array = merge_sort(array[middle:])
    return merge(left_array, right_array)
