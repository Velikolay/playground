from typing import List


def quick_sort(arr: List[int]) -> None:
    quick_sort_rec(arr, 0, len(arr) - 1)


def quick_sort_rec(arr: List[int], start: int, end: int) -> None:
    if start < end:
        pivot_idx = partition(arr, start, end)
        quick_sort_rec(arr, start, pivot_idx - 1)
        quick_sort_rec(arr, pivot_idx + 1, end)


def partition(arr: List[int], start: int, end: int) -> int:
    pivot = arr[end]
    i = start
    for j in range(start, end):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


if __name__ == "__main__":
    lst = [2, 8, 5, 11, 22, 3]
    # lst = [5, 2]
    quick_sort(lst)
    print(lst)
