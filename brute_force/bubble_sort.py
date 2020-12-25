def bubble_sort(number_list):
    length = len(number_list)

    if length < 2:
        return number_list

    i = 0
    while i < length:
        i += 1
        for j in range(0, length - 1):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
    return number_list
