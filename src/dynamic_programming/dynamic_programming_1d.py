import time


def time_record(func):
    def wrapper(*args):
        time1 = time.time()
        result = func(*args)
        time2 = time.time()
        print("time used: ", time2 - time1)
        return result
    return wrapper


def fibonacci(n):
    result = []
    for i in range(n + 1):
        if i <= 1:
            result.append(i)
        else:
            result.append(result[i - 1] + result[i - 2])
    return result[-1]


print(fibonacci(9))


def max_length_ascending_subarray(array):
    if not array:
        return 0
    m = [1]
    max_length = 1
    for i in range(1, len(array)):
        if array[i] >= array[i - 1]:
            m.append(m[-1] + 1)
            max_length = m[-1] if m[-1] > max_length else max_length
        else:
            m.append(1)
    return max_length


test_array = [7, 2, 3, 1, 5, 8, 8, 9, 6]
print(max_length_ascending_subarray(test_array))


# the rope must have one cut at least
@time_record
def max_product_of_rope1(rope_length):
    if rope_length <= 1:
        return -1
    result = [-1, -1]
    for length in range(2, rope_length + 1):
        max_product = 0
        for length_of_shorter in range(1, length // 2 + 1):
            length_of_longer = length - length_of_shorter
            cur_product = max(length_of_shorter, result[length_of_shorter]) * max(length_of_longer, result[length_of_longer])
            max_product = max(max_product, cur_product)
        result.append(max_product)
    return result[-1]


# assume left part doesn't have cut
@time_record
def max_product_of_rope2(rope_length):
    if rope_length <= 1:
        return -1
    result = [-1, -1]
    for length in range(2, rope_length + 1):
        max_product = 0
        for left_length in range(1, length):
            right_length = length - left_length
            cur_product = left_length * max(right_length, result[right_length])
            max_product = max(cur_product, max_product)
        result.append(max_product)
    return result[-1]


def max_product_of_rope_recursion(rope_length):
    if rope_length == 1:
        return -1
    max_product = 0
    for left_length in range(1, rope_length):
        right_length = rope_length - left_length
        cur_product = left_length * max(right_length, max_product_of_rope_recursion(right_length))
        max_product = max(max_product, cur_product)
    return max_product


print('max product of rope:')
print(max_product_of_rope1(20))
print(max_product_of_rope2(100))
print("recursion: ", max_product_of_rope_recursion(10))


def jump_to_end_reverse(jump_steps):
    if not jump_steps:
        return True
    m = [True]
    jump_steps.reverse()
    for cur_idx in range(1, len(jump_steps)):
        temp = False
        max_steps = min(jump_steps[cur_idx], cur_idx)
        for steps in range(1, max_steps + 1):
            if m[cur_idx - steps]:
                temp = True
                break
        m.append(temp)
    jump_steps.reverse()
    return m[-1]


def jump_to_end(jump_steps):
    if not jump_steps:
        return True
    m = [True]
    for idx in range(1, len(jump_steps)):
        temp = False
        for pre_idx in range(idx):
            if m[pre_idx] and jump_steps[pre_idx] >= idx - pre_idx:
                temp = True
                break
        m.append(temp)
    return m[-1]


def min_jump_reverse(jump_steps):
    if not jump_steps:
        return 0
    jump_steps.reverse()
    m = [0]
    for idx in range(1, len(jump_steps)):
        max_steps = min(idx, jump_steps[idx])
        min_jump = float('inf')
        for steps in range(1, max_steps + 1):
            if m[idx - steps] < min_jump:
                min_jump = m[idx - steps]
        m.append(min_jump + 1)
        print(m)
    jump_steps.reverse()
    return m[-1]


print('jump to the end:')
test_jump = [2, 1, 1, 2, 4, 2]
print(jump_to_end(test_jump))
print(jump_to_end_reverse(test_jump))
print(min_jump_reverse(test_jump))


def largest_sum_subarray(array):
    if not array:
        return 0
    m = [array[0]]
    global_max = m[-1]
    final_left = final_right = temp_left = 0
    for idx in range(1, len(array)):
        if m[-1] > 0:
            m.append(m[-1] + array[idx])
        else:
            m.append(array[idx])
            temp_left = idx
        if m[-1] > global_max:
            global_max = m[-1]
            final_left = temp_left
            final_right = idx
    return global_max, (final_left, final_right)


test_list = [1, 2, 3, -1, -20, 1, -4]
print(largest_sum_subarray(test_list))


def compose_text(text, dictionary):
    if not text:
        return True
    m = [text[0] in dictionary]
    for idx in range(1, len(text)):
        temp = False
        for left_end in range(idx):
            if m[left_end] and text[left_end + 1:idx + 1] in dictionary:
                temp = True
                break
        if text[:idx + 1] in dictionary:
            temp = True
        m.append(temp)
    return m[-1]


test_dict = {'bob', 'cat', 'rob'}
test_text = 'bobcataob'
print(compose_text(test_text, test_dict))
