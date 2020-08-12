# 08/12/2020


def selection_sort(array):
    if len(array) == 0:
        return array
    for head_of_unsorted in range(len(array) - 1):
        index_min = head_of_unsorted
        for index in range(head_of_unsorted + 1, len(array)):
            index_min = index if array[index_min] > array[index] else index_min
        array[index_min], array[head_of_unsorted] = array[head_of_unsorted], array[index_min]
    return array


unsortedArray = [-2, 5, 7, 3, 6]
sortedArray = selection_sort(unsortedArray)
print(sortedArray)
