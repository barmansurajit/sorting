import numpy


# n = number of elements
# k = range, example 0 - 9 so k is 9

def counting_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # determine the size of the count array
    k = numpy.max(arr)

    # initialize the count array
    count = numpy.zeros(k + 1, dtype=numpy.int8).tolist()

    # determine the number of occurrences
    for i in range(0, n):
        count[arr[i]] += 1

    # determine the positions
    for j in range(1, k + 1):
        count[j] += count[j - 1]

    # sort
    brr = numpy.zeros(n, dtype=numpy.int8).tolist()
    for k in range(n - 1, -1, -1):
        count[arr[k]] = count[arr[k]] - 1
        brr[count[arr[k]]] = arr[k]
    return brr

