# 6/28/2020


def binary_search_recursion(array, left_index, right_index, target) -> int:
    if left_index > right_index:
        return -1
    mid_index = left_index + (right_index - left_index) // 2
    if array[mid_index] > target:
        return binary_search_recursion(array, left_index, mid_index - 1, target)
    elif array[mid_index] < target:
        return binary_search_recursion(array, mid_index + 1, right_index, target)
    else:
        return mid_index


def binary_search_iteration(array, target):
    if len(array) == 0:
        return -1
    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] < target:
            left_index = mid_index + 1
        elif array[mid_index] > target:
            right_index = mid_index - 1
        else:
            return mid_index
    return -1


def binary_search_2d_iteration(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    row_num = len(matrix)
    column_num = len(matrix[0])
    left_index = 0
    right_index = row_num * column_num - 1
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if matrix[mid_index // column_num][mid_index % column_num] > target:
            right_index = mid_index - 1
        elif matrix[mid_index // column_num][mid_index % column_num] < target:
            left_index = mid_index + 1
        else:
            return [mid_index // column_num, mid_index % column_num]
    return None


def binary_search_2d_recursion(matrix, target, left_index, right_index, column_num):
    if left_index > right_index:
        return None
    mid_index = left_index + (right_index - left_index) // 2
    if matrix[mid_index // column_num][mid_index % column_num] > target:
        right_index = mid_index - 1
    elif matrix[mid_index // column_num][mid_index % column_num] < target:
        left_index = mid_index + 1
    else:
        return [mid_index // column_num, mid_index % column_num]
    return binary_search_2d_recursion(matrix, target, left_index, right_index, column_num)


def binary_search_closet_index1(array, target):
    if len(array) == 0:
        return -1
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index - 1:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] > target:
            right_index = mid_index
        elif array[mid_index] < target:
            left_index = mid_index
        else:
            return mid_index

    # post processing
    if abs(target - array[left_index]) <= abs(target - array[right_index]):
        return left_index
    else:
        return right_index


def binary_search_closet_index2(array, target):
    if len(array) == 0:
        return -1
    left_index = 0
    right_index = len(array) - 1
    closet_index = 0
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if abs(target - array[mid_index]) < abs(target - array[closet_index]):
            closet_index = mid_index
        if array[mid_index] > target:
            right_index = mid_index - 1
        elif array[mid_index] < target:
            left_index = mid_index + 1
        else:
            return mid_index
    return closet_index


def binary_search_first_occur_index1(array, target):
    if len(array) == 0:
        return -1
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index - 1:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] > target:
            right_index = mid_index - 1
        elif array[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index

    # post processing
    if array[left_index] == target:
        return left_index
    elif array[right_index] == target:
        return right_index
    else:
        return -1


def binary_search_first_occur_index2(array, target):
    if len(array) == 0:
        return -1
    left_index = 0
    right_index = len(array) - 1
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] > target:
            right_index = mid_index - 1
        elif array[mid_index] < target:
            left_index = mid_index + 1
        else:
            if mid_index > 0 and array[mid_index - 1] == target:
                right_index = mid_index - 1
            else:
                return mid_index
    return -1


# assuming keys in dictionary in consecutive starting from 1, values are in ascending order
# assuming the dictionary at least has 1 key:value pair
def search_in_unknown_size_dictionary(dictionary, target):
    if not dictionary:
        return None
    left_index = 1
    right_index = 1
    while right_index in dictionary and dictionary[right_index] < target:
        left_index = right_index + 1
        right_index = right_index * 2
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if mid_index in dictionary:
            if dictionary[mid_index] < target:
                left_index = mid_index + 1
            elif dictionary[mid_index] > target:
                right_index = mid_index - 1
            else:
                return mid_index
        else:
            right_index = mid_index - 1
    return -1


def binary_search_largest_smaller_equal(array, target):
    if len(array) == 0:
        return None
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index - 1:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] < target:
            left_index = mid_index
        elif target < array[mid_index]:
            right_index = mid_index - 1
        else:
            return mid_index
    if array[right_index] <= target:
        return right_index
    else:
        return left_index


original =[2, 4, 6, 8, 9, 14, 14, 16, 17, 25, 27, 34, 56]
print(binary_search_recursion(original, 0, len(original) - 1, 6))
print(binary_search_closet_index2(original, 10))
print(binary_search_first_occur_index1(original, 14))
print(binary_search_first_occur_index2(original, 14))
print(binary_search_largest_smaller_equal(original, 10))

test_matrix = [[1, 4, 6], [8, 9, 12], [24, 35, 67]]
print(binary_search_2d_iteration(test_matrix, 67))
print(binary_search_2d_recursion(test_matrix, 67, 0, len(test_matrix) * len(test_matrix[0]) - 1, len(test_matrix[0])))

test_dict = {1: 2, 2: 4, 3: 5, 4 : 8, 5: 10, 6: 19}
print(search_in_unknown_size_dictionary(test_dict, 10))
