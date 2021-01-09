import math


def dropped_request(time_list):
    if len(time_list) == 0:
        return 0
    dropped_num = 0
    for index in range(len(time_list)):
        case1 = index >= 3 and time_list[index] - time_list[index - 3] + 1 <= 1
        case2 = index >= 20 and time_list[index] - time_list[index - 20] + 1 <= 10
        case3 = index >= 60 and time_list[index] - time_list[index - 60] + 1 <= 60
        if case1 or case2 or case3:
            dropped_num += 1
    return dropped_num


time_spots = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
print(dropped_request(time_spots))


# Given a positive integer n, how many ways can we write it as a sum of consecutive positive integers?
def consecutive_numbers_sum(n):
    num_of_seq = 0
    for sequence_size in range(2, int(0.5 + 0.5 * math.sqrt(1 + 8 * n))):
        temp = n - (sequence_size - 1) * sequence_size // 2
        if temp % sequence_size == 0:
            num_of_seq += 1
    return num_of_seq


print(consecutive_numbers_sum(15))


def find_before_matrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    before_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    before_matrix[0][0] = matrix[0][0]
    for index in range(1, len(matrix[0])):
        before_matrix[0][index] = matrix[0][index] - matrix[0][index - 1]
    for index in range(1, len(matrix)):
        before_matrix[index][0] = matrix[index][0] - matrix[index - 1][0]
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            before_matrix[row][col] = matrix[row][col] - matrix[row - 1][col]\
                                      - matrix[row][col - 1] + matrix[row - 1][col - 1]
    return before_matrix


after_matrix = [[1, 2], [3, 4]]
print(find_before_matrix(after_matrix))


# assume all bids greater than 0
def get_0_allotted_user(bids, total_shares):
    if len(bids) == 0:
        return 0
    elif total_shares == 0:
        return len(bids)
    bids.sort(key=lambda bid: (-1 * bid[2], bid[3]))
    for index in range(len(bids)):
        if total_shares <= 0:
            break
        total_shares -= bids[index][1]
    user_list = []
    while index < len(bids):
        user_list.append(bids[index][0])
        index += 1
    return user_list


bids = [[1, 5, 5, 0], [2, 7, 8, 1], [3, 7, 5, 1], [4, 10, 3, 3]]
print(get_0_allotted_user(bids, 13))
