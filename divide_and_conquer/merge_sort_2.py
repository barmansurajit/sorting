
def merge(arr, lb, mid, ub):
    i = lb
    j = mid + 1
    result = []

    while i <= mid and j <= ub:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    while j <= ub:
        result.append(arr[j])
        j += 1
    while i <= mid:
        result.append(arr[i])
        i += 1

    return result


def merge_sort(arr, lb, ub):
    if lb < ub:
        mid = lb + (ub - lb) // 2
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid + 1, ub)
        return merge(arr, lb, mid, ub)
