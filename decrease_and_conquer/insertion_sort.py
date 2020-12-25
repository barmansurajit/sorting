def insertion_sort_recursive(number_list, n):
    if n <= 1:
        return

    insertion_sort_recursive(number_list, n - 1)

    j = n - 2
    while j >= 0 and number_list[j] > number_list[j + 1]:
        number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
        j -= 1


def insertion_sort_recursive_2(number_list, n):
    if n <= 1:
        return

    insertion_sort_recursive_2(number_list, n - 1)

    last = number_list[n - 1]
    j = n - 2

    while j >= 0 and number_list[j] > last:
        number_list[j + 1] = number_list[j]
        j -= 1

    number_list[j + 1] = last


def insertion_sort_iterative(number_list):
    n = len(number_list)
    if n <= 1:
        return

    for i in range(1, n):
        ith = number_list[i]
        j = i - 1

        while j >= 0 and number_list[j] > ith:
            number_list[j + 1] = number_list[j]
            j -= 1

        number_list[j + 1] = ith
