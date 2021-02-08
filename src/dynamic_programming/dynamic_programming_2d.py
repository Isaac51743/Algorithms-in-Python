def min_step_transform(text1, text2):
    if not text1:
        return len(text2)
    elif not text2:
        return len(text1)
    m = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
    for idx in range(len(text1) + 1):
        m[0][idx] = idx
    for idx in range(len(text2) + 1):
        m[idx][0] = idx
    for row in range(1, len(text2) + 1):
        for col in range(1, len(text1) + 1):
            if text1[col - 1] == text2[row - 1]:
                m[row][col] = m[row - 1][col - 1]
            else:
                m[row][col] = min(m[row - 1][col], m[row][col - 1], m[row - 1][col - 1]) + 1
    return m[-1][-1]


def min_step_transform_adv(text1, text2):
    if not text1:
        return len(text2)
    elif not text2:
        return len(text1)
    pre = [i for i in range(len(text1) + 1)]
    row_num = 1

    while row_num <= len(text2):
        cur = [row_num]
        for idx in range(1, len(text1) + 1):
            if text1[idx - 1] == text2[row_num - 1]:
                cur.append(pre[idx - 1])
            else:
                cur.append(1 + min(pre[idx - 1], cur[idx - 1], pre[idx]))
        pre = cur
        row_num += 1
    return pre[-1]


test_text1 = 'zhaoyuehng'
test_text2 = 'zhoyuehang'
print(min_step_transform(test_text1, test_text2))
print("saved space: ", min_step_transform_adv(test_text1, test_text2))


def max_square(matrix):
    if not matrix or not matrix[0]:
        return 0
    max_length = 0
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][col]:
                matrix[row][col] = 1 + min(matrix[row - 1][col], matrix[row][col - 1], matrix[row - 1][col - 1])
                if matrix[row][col] > max_length:
                    max_length = matrix[row][col]
    return max_length


edge_length = 6
test_matrix = [[0] * edge_length for _ in range(edge_length)]
for i in range(2, 5):
    for j in range(2, 5):
        test_matrix[i][j] = 1
test_matrix[0][0] = 1
test_matrix[1][5] = 1
print(max_square(test_matrix))

