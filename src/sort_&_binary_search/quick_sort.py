# 08/12/2020


def quick_sort(array, start_index, end_index):
    if start_index >= end_index:
        return
    left_index = start_index
    right_index = end_index - 1
    while left_index <= right_index:
        if array[left_index] < array[end_index]:
            left_index += 1
        else:
            array[left_index], array[right_index] = array[right_index], array[left_index]
            right_index -= 1
    array[left_index], array[end_index] = array[end_index], array[left_index]
    quick_sort(array, start_index, right_index)
    quick_sort(array, left_index + 1, end_index)


original = [1, 74, 6, 7, 3, 45, 8, 3, 7, 4, 8, 68, 23]
quick_sort(original, 0, len(original) - 1)
print(original)