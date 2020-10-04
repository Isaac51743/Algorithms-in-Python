# 09/08/2020


# assuming array is not None and has >= 1 element
# helper is an assistant array with the same length of original array
def merge_sort(array, start_index, end_index, helper):
    if start_index == end_index:
        return
    mid_index = start_index + (end_index - start_index) // 2
    merge_sort(array, start_index, mid_index, helper)
    merge_sort(array, mid_index + 1, end_index, helper)
    _merge(array, start_index, mid_index, end_index, helper)


def _merge(array, start_index, mid_index, end_index, helper):
    helper[start_index:end_index + 1] = array[start_index:end_index + 1]
    index1 = index3 = start_index
    index2 = mid_index + 1
    while index1 <= mid_index and index2 <= end_index:
        if helper[index1] < helper[index2]:
            array[index3] = helper[index1]
            index1 += 1
        else:
            array[index3] = helper[index2]
            index2 += 1
        index3 += 1
    # if the index of subarray1 haven't arrive mid index
    while index1 <= mid_index:
        array[index3] = helper[index1]
        index1 += 1
        index3 += 1
    # if index of subarray2 haven't arrive end_index, no operation needed


original1 = [1, 2, 4, 5, 3, 5, 7, 2, 0, 9, 6]
helper1 = [0] * len(original1)
merge_sort(original1, 0, len(original1) - 1, helper1)
print(original1)

