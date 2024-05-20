from algorithms.utils import swap


def bubble_sort(array: list[int]) -> list[int]:
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i,  -1):
            if array[i] > array[j]:
                swap(array, i, j)
    return array
