from random import randint


def quick_sort_lomuto(arr):
    n = len(arr)
    if n <= 1:
        return arr

    quick_sort_helper(arr, 0, n - 1)


def quick_sort_helper(arr, start, end):
    if start >= end:
        return

    random_index = randint(start, end)

    arr[random_index], arr[start] = arr[start], arr[random_index]
    pivot = arr[start]
    smaller = start

    for bigger in range(start + 1, end + 1):
        if arr[bigger] < pivot:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]

    arr[start], arr[smaller] = arr[smaller], arr[start]
    quick_sort_helper(arr, start, smaller - 1)
    quick_sort_helper(arr, smaller + 1, end)


def quick_sort_hoare(arr):
    n = len(arr)
    if n <= 1:
        return arr