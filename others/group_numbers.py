def solve(arr):

    if not arr or len(arr) == 0:
        return arr

    curr_ind = 0
    even_ind = 0
    n = len(arr)

    while curr_ind < n:
        if arr[curr_ind] % 2 == 0:
            arr[curr_ind], arr[even_ind] = arr[even_ind], arr[curr_ind]
            even_ind = even_ind + 1
            curr_ind = curr_ind + 1
        else:
            curr_ind = curr_ind + 1


array = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Pre-grouped numbers {array}")
solve(array)
print(f"Post-grouped numbers {array}")
