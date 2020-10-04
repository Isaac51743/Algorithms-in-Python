# 09/08/2020


def binary_search_recursion(array, left_index, right_index, target) -> int:
    if left_index > right_index:
        return -1
    mid_index = left_index + (right_index - left_index) // 2
    if array[mid_index] < target:
        return binary_search_recursion(array, mid_index + 1, right_index, target)
    elif array[mid_index] > target:
        return binary_search_recursion(array, left_index, mid_index - 1, target)
    else:
        return mid_index


def binary_search_iteration(array, target):
    if len(array) == 0:
        return -1
    left_bound = 0
    right_bound = len(array) - 1
    while left_bound <= right_bound:
        mid_index = left_bound + (right_bound - left_bound) // 2
        if array[mid_index] < target:
            left_bound = mid_index + 1
        elif array[mid_index] > target:
            right_bound = mid_index - 1
        else:
            return mid_index
    return -1


# "return a, b" equals to "return (a, b)", "return a" doesn't equal to "return (a)"
def binary_search_2d_iteration(matrix, target) -> tuple:
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return -1, -1
    width = len(matrix[0])
    height = len(matrix)
    left_index = 0
    right_index = width * height - 1
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        row = mid_index // width
        column = mid_index % width
        if matrix[row][column] < target:
            left_index = mid_index + 1
        elif matrix[row][column] > target:
            right_index = mid_index - 1
        else:
            return row, column
    return -1, -1


def binary_search_2d_recursion(matrix, target, left_index, right_index) -> tuple:
    if left_index > right_index:
        return -1, -1
    width = len(matrix[0])
    mid_index = left_index + (right_index - left_index) // 2
    row = mid_index // width
    column = mid_index % width
    if matrix[row][column] > target:
        return binary_search_2d_recursion(matrix, target, left_index, mid_index - 1)
    elif matrix[row][column] < target:
        return binary_search_2d_recursion(matrix, target, mid_index + 1, right_index)
    else:
        return row, column


# assume left_index < right_index, array is valid
def binary_search_closet_index_recursion(array, target, left_index, right_index):
    if left_index == right_index - 1:
        return left_index if abs(array[left_index] - target) < abs(array[right_index] - target) else right_index

    mid_index = left_index + (right_index - left_index) // 2
    if array[mid_index] > target:
        return binary_search_closet_index_recursion(array, target, left_index, mid_index)
    elif array[mid_index] < target:
        return binary_search_closet_index_recursion(array, target, mid_index, right_index)
    else:
        return mid_index


def binary_search_closet_index1(array, target) -> int:
    if len(array) == 0:
        return -1
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index - 1:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] < target:
            left_index = mid_index
        elif array[mid_index] > target:
            right_index = mid_index
        else:
            return mid_index

    # final range with length 2
    return left_index if abs(array[left_index] - target) < abs(array[right_index] - target) else right_index


def binary_search_closet_index2(array, target) -> int:
    if len(array) == 0:
        return -1
    left_index = 0
    right_index = len(array) - 1
    closet_index = 0
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        if abs(array[mid_index] - target) < abs(array[closet_index] - target):
            closet_index = mid_index
        if array[mid_index] < target:
            left_index = mid_index + 1
        elif array[mid_index] > target:
            right_index = mid_index - 1
        else:
            return mid_index
    return closet_index


def binary_search_first_occur_index1(array, target) -> int:
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
        elif mid_index > 0 and array[mid_index - 1] == target:
            right_index = mid_index - 1
        else:
            return mid_index
    return -1


def binary_search_first_occur_index2(array, target) -> int:
    if len(array) == 0:
        return -1
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index - 1:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] < target:
            left_index = mid_index + 1
        elif array[mid_index] > target:
            right_index = mid_index - 1
        else:
            right_index = mid_index

    # final range with length 2 or 1
    # post processing
    if array[left_index] == target:
        return left_index
    elif array[right_index] == target:
        return right_index
    else:
        return -1


def binary_search_largest_smaller_or_equal(array, target):
    if len(array) == 0:
        return -1
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index - 1:
        mid_index = left_index + (right_index - left_index) // 2
        if array[mid_index] < target:
            left_index = mid_index
        elif array[mid_index] > target:
            right_index = mid_index - 1
        else:
            return mid_index
    if array[right_index] <= target:
        return right_index
    elif array[left_index] <= target:
        return left_index
    else:
        return -1


# assuming keys in dictionary in consecutive starting from 1, values are in ascending order
# assuming the dictionary at least has 1 key:value pair
def search_in_unknown_size_dictionary(dictionary, target) -> int:
    if len(dictionary) == 0:
        return -1
    left_key = 1
    right_key = 1
    # expand the search range
    while right_key in dictionary and dictionary[right_key] < target:
        left_key = right_key + 1
        right_key *= 2
    # shrink the right bound
    while right_key not in dictionary:
        right_key -= 1
    # binary search
    while left_key <= right_key:
        mid_key = left_key + (right_key - left_key) // 2
        if dictionary[mid_key] < target:
            left_key = mid_key + 1
        elif dictionary[mid_key] > target:
            right_key = mid_key - 1
        else:
            return mid_key
    return -1


original =[2, 4, 6, 8, 9, 14, 14, 16, 17, 25, 27, 34, 56]
print("binary search(no valid result maybe):")
print(binary_search_recursion(original, 0, len(original) - 1, 9))
print(binary_search_iteration(original, 2))
print("search closet")
print(binary_search_closet_index1(original, 15))
print(binary_search_closet_index2(original, 15))
print(binary_search_closet_index_recursion(original, 15, 0, len(original) - 1))
print("search first occur(no valid result maybe):")
print(binary_search_first_occur_index1(original, 10))
print(binary_search_first_occur_index2(original, 14))
print("search largest smaller or equal number(no valid result maybe):")
test = [4, 15, 26]
print(binary_search_largest_smaller_or_equal(test, 10))

test_matrix = [[1, 4, 6], [8, 9, 12], [24, 35, 67]]
print("binary search in matrix:")
print(binary_search_2d_iteration(test_matrix, 24))
print(binary_search_2d_recursion(test_matrix, 67, 0, len(test_matrix) * len(test_matrix[0]) - 1))
# conclusion:
# 1. the final range, when "while left_index < right_index - 1"
# 2. whether the valid result exists

test_dict = {1: 2, 2: 4, 3: 5, 4: 8, 5: 10, 6: 19}
print("search in dictionary of unknown size:")
print(search_in_unknown_size_dictionary(test_dict, 11))
