def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr

    # identify the mid-point of the array
    mid = int(0 + (n - 0) / 2)

    # partition into two halves
    # sort both the sides
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge the sorted partitions
    return merge(left, right)


def merge(left, right):
    result = []

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# def merge_sort_helper(arr, start, end):
#     if start >= end:
#         return
#
#     mid = int((start + end)/2)
#     merge_sort_helper(arr, start, mid)
#     merge_sort_helper(arr, mid + 1, end)
#
#     i = start
#     j = mid + 1
#
#     aux = []
#     while i < mid and j < end:
#         if arr[i] <= arr[j]:
#             aux.append(arr[i])
#             i += 1
#         else:
#             aux.append(arr[j])
#             j += 1
#
#     while i < mid:
#         aux.append(arr[i])
#         i += 1
#     while j < end:
#         aux.append(arr[j])
#         j += 1
#
#     return aux
