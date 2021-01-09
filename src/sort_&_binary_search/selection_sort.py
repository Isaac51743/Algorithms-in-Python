# 12/18/2020
def selection_sort(array):
    if len(array) == 0:
        return array
    for unsorted_head in range(len(array) - 1):
        min_idx = unsorted_head
        for idx in range(unsorted_head, len(array)):
            min_idx = idx if array[idx] < array[min_idx] else min_idx
        array[min_idx], array[unsorted_head] = array[unsorted_head], array[min_idx]
    return array


def selection_sort_recursion(array, unsorted_head):
    if len(array) == 0:
        return array
    # base case
    if unsorted_head == len(array) - 1:
        return array

    # recursion rule
    min_idx = unsorted_head
    for idx in range(unsorted_head, len(array)):
        min_idx = idx if array[idx] < array[min_idx] else min_idx
    array[unsorted_head], array[min_idx] = array[min_idx], array[unsorted_head]
    return selection_sort_recursion(array, unsorted_head + 1)


unsortedArray = [-2, 5, 7, 3, 6]
print(selection_sort(unsortedArray))
print(selection_sort_recursion(unsortedArray, 0))
