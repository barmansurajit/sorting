from typing import List


def merge(array_1: List[int], array_2: List[int]) -> List[int]:
    if array_1 is None and array_2 is None:
        return None

    if array_1 is None and array_2 is not None:
        return array_2

    if array_1 is not None and array_2 is None:
        return array_1

    result = []

    i = j = 0

    while i < len(array_1) and j < len(array_2):
        if array_1[i] <= array_2[j]:
            result.append(array_1[i])
            i += 1
        else:
            result.append(array_2[j])
            j += 1

    while i < len(array_1):
        result.append(array_1[i])
        i += 1
    while j < len(array_2):
        result.append(array_2[j])
        j += 1

    return result


def merge_2(array_1: List[int], array_2: List[int]) -> List[int]:
    len_array_1 = len(array_1)
    len_array_2 = len(array_2)

    i = len_array_1 - 1
    j = len_array_2 - 1

    if len_array_2 > len_array_1:
        k = len_array_2 - 1
        while j >= 0 and array_2[j] == 0:
            j = j - 1
    else:
        k = len_array_1 - 1
        while i >= 0 and array_1[i] == 0:
            i = i - 1

    while i >= 0 and j >= 0 and k >= 0:
        if array_1[i] >= array_2[j]:
            array_2[k] = array_1[i]
            i = i - 1
        elif array_2[j] >= array_1[i]:
            array_2[k] = array_2[j]
            j = j - 1
        k = k - 1

    while i >= 0:
        array_2[k] = array_1[i]
        i = i - 1
        k = k - 1

    while j >= 0:
        array_2[k] = array_2[j]
        j = j - 1
        k = k - 1

    # print(i, j, k)
    return array_2


if __name__ == "__main__":
    print(f"{merge_2([100, 100, 200, 300, 300, 400, 400], [90, 100, 100, 200, 200, 450, 450, 0, 0, 0, 0, 0, 0, 0])}")
