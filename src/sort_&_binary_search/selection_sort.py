# 09/08/2020


def selection_sort(array):
    if len(array) == 0:
        return array
    for start_of_unsorted in range(len(array) - 1):
        min_index = start_of_unsorted
        for i in range(start_of_unsorted + 1, len(array)):
            if array[i] < array[min_index]:
                min_index = i
        array[min_index], array[start_of_unsorted] = array[start_of_unsorted], array[min_index]
    return array


unsortedArray = [-2, 5, 7, 3, 6]
sortedArray = selection_sort(unsortedArray)
print(sortedArray)
