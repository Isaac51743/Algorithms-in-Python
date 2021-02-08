def longest_1(array):
    if not array:
        return 0
    m = [array[0]]
    max_length = m[-1]
    left = 0 if array[0] else 1
    final_left = final_right = -1
    for idx in range(1, len(array)):
        if array[idx]:
            m.append(m[-1] + 1)
            if max_length < m[-1]:
                max_length = m[-1]
                final_left = left
                final_right = idx
        else:
            m.append(0)
            left = idx + 1
    return max_length, final_left, final_right


test_array1 = [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0 ,0, 0]
print(longest_1(test_array1))


def max_storage_water(array):
    if not array:
        return 0
    left_based = [array[0]]
    right_based = [array[-1]]
    for idx in range(1, len(array)):
        left_based.append(max(left_based[-1], array[idx]))
        right_based.append(max(right_based[-1], array[-1 - idx]))
    right_based.reverse()
    storage = 0
    for idx in range(len(array)):
        storage += min(left_based[idx], right_based[idx]) - array[idx]
    return storage


fence1 = [5, -1, 2, -1, 5, 5]
print(max_storage_water(fence1))


def matrix_print(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            print(matrix[row][column], end=' ')
        print()


def find_largest_cross(matrix):
    if not matrix or not matrix[0]:
        return -1, -1, -1
    left_arm = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    right_arm = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    top_arm = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    bottom_arm = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row in range(len(matrix)):
        left_arm[row][0] = matrix[row][0]
        right_arm[row][-1] = matrix[row][-1]
        for idx in range(1, len(matrix[0])):
            if matrix[row][idx]:
                left_arm[row][idx] = left_arm[row][idx - 1] + 1
            else:
                left_arm[row][idx] = 0
            if matrix[row][-1 - idx]:
                right_arm[row][-1 - idx] = right_arm[row][-idx] + 1
            else:
                right_arm[row][-1 - idx] = 0
    for col in range(len(matrix[0])):
        top_arm[0][col] = matrix[0][col]
        bottom_arm[-1][col] = matrix[-1][col]
        for idx in range(1, len(matrix)):
            if matrix[idx][col]:
                top_arm[idx][col] = top_arm[idx - 1][col] + 1
            else:
                top_arm[idx][col] = 0
            if matrix[-1 - idx][col]:
                bottom_arm[-1 - idx][col] = bottom_arm[-idx][col] + 1
            else:
                bottom_arm[-1 - idx][col] = 0
    final_row = final_col = -1
    max_arm = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if min(left_arm[row][col], right_arm[row][col], top_arm[row][col], bottom_arm[row][col]) > max_arm:
                final_row = row
                final_col = col
                max_arm = min(left_arm[row][col], right_arm[row][col], top_arm[row][col], bottom_arm[row][col])
    return max_arm - 1, final_row, final_col


test_matrix1 = [[0 for _ in range(10)] for _ in range(10)]
for row in range(5):
    test_matrix1[row][5//2] = 1
for column in range(5):
    test_matrix1[5//2][column] = 1
matrix_print(test_matrix1)
print(find_largest_cross(test_matrix1))


def find_largest_hollow_square(matrix):
    if not matrix or not matrix[0]:
        return -1, -1, -1
    top_bound = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    bottom_bound = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    left_bound = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    right_bound = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row in range(len(matrix)):
        top_bound[row][-1] = matrix[row][-1]
        bottom_bound[row][0] = matrix[row][0]
        for idx in range(1, len(matrix[0])):
            if matrix[row][-1 - idx]:
                top_bound[row][-1 - idx] = top_bound[row][-idx] + 1
            else:
                top_bound[row][-1 - idx] = 0
            if matrix[row][idx]:
                bottom_bound[row][idx] = bottom_bound[row][idx - 1] + 1
            else:
                bottom_bound[row][idx] = 0
    for col in range(len(matrix[0])):
        left_bound[-1][col] = matrix[-1][col]
        right_bound[0][col] = matrix[0][col]
        for idx in range(1, len(matrix)):
            if matrix[-1 - idx][col]:
                left_bound[-1 - idx][col] = left_bound[-idx][col] + 1
            else:
                left_bound[-1 - idx][col] = 0
            if matrix[idx][col]:
                right_bound[idx][col] = right_bound[idx - 1][col] + 1
            else:
                right_bound[idx][col] = 0
    max_length = 0
    row_top_left = col_top_left = -1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for shift in range(min(len(matrix) - 1 - row, len(matrix[0]) - 1 - col, min(left_bound[row][col], top_bound[row][col]) - 1), -1, -1):
                if max_length < shift + 1 <= min(bottom_bound[row + shift][col + shift], right_bound[row + shift][col + shift]):
                    max_length = shift + 1
                    row_top_left = row
                    col_top_left = col
                    break
    return max_length, row_top_left, col_top_left


test_matrix2 = [[0 for _ in range(10)] for _ in range(10)]
for i in range(4):
    test_matrix2[1][1 + i] = 1
for i in range(4):
    test_matrix2[4][1 + i] = 1
for i in range(4):
    test_matrix2[1 + i][1] = 1
for i in range(4):
    test_matrix2[1 + i][4] = 1
matrix_print(test_matrix2)
print(find_largest_hollow_square(test_matrix2))


def path_prefix(array):
    if not array:
        return []
    m = [array[0]]
    for idx in range(1, len(array)):
        m.append(m[-1] + array[idx])
    return m


def sum_subarray(path_prefix, start_idx, end_idx):
    if not path_prefix or start_idx > end_idx or start_idx < 0 or end_idx >= len(path_prefix):
        print("invalid input!")
        return -1
    if start_idx == 0:
        return path_prefix[end_idx]
    return path_prefix[end_idx] - path_prefix[start_idx - 1]


test_array2 = [1, 2, 4, 2, 14, 23, 5, 3]
print("path prefix: ", sum_subarray(path_prefix(test_array2), 2, 5))


def find_largest_submatrix(matrix):
    if not matrix or not matrix[0]:
        return None
    m = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    m[0][0] = matrix[0][0]
    for col in range(1, len(matrix[0])):
        m[0][col] = m[0][col - 1] + matrix[0][col]
    for row in range(1, len(matrix)):
        m[row][0] = m[row - 1][0] + matrix[row][0]
    for row in  range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            m[row][col] = matrix[row][col] + m[row - 1][col] + m[row][col - 1] - m[row - 1][col - 1]
    max_sum = float("-inf")
    # matrix_print(m)
    top_left = bottom_right = None
    for row_start in range(len(matrix)):
        for row_end in range(row_start, len(matrix)):
            for col_start in range(len(matrix[0])):
                for col_end in range(col_start, len(matrix[0])):
                    temp_sum = m[row_end][col_end]
                    if row_start > 0:
                        temp_sum -= m[row_start - 1][col_end]
                    if col_start > 0:
                        temp_sum -= m[row_end][col_start - 1]
                    if row_start > 0 and col_start > 0:
                        temp_sum += m[row_start - 1][col_start - 1]
                    if max_sum < temp_sum:
                        top_left = (row_start, col_start)
                        bottom_right = (row_end, col_end)
                        max_sum = temp_sum
    return max_sum, top_left, bottom_right


test_matrix3 = ([[1, 1, 1, -100, 2, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 99, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 2, 1, 1],
                        [1, 1, 1,  -100, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1,  -100, 1, 1, 1, 1, 1, 1]])
print(find_largest_submatrix(test_matrix3))

