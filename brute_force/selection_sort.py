def selection_sort(number_list):
    length = len(number_list)

    if length < 2:
        return number_list

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if number_list[j] < number_list[min_index]:
                min_index = j
        number_list[i], number_list[min_index] = number_list[min_index], number_list[i]

    return number_list
