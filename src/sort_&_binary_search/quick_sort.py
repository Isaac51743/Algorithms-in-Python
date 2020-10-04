# 09/08/2020


def quick_sort(array, start_index, end_index):
    if start_index >= end_index:
        return
    left_bound = start_index
    right_bound = end_index - 1
    while left_bound <= right_bound:
        if array[left_bound] < array[end_index]:
            left_bound += 1
        else:
            array[left_bound], array[right_bound] = array[right_bound], array[left_bound]
            right_bound -= 1
    array[left_bound], array[end_index] = array[end_index], array[left_bound]
    quick_sort(array, start_index, left_bound - 1)
    quick_sort(array, left_bound + 1, end_index)


original = [1, 74, 6, 7, 3, 45, 8, 3, 7, 4, 8, 68, 23]
quick_sort(original, 0, len(original) - 1)
print(original)