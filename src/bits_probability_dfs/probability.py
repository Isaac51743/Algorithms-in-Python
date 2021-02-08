import random as r
import heapq as hq


def shuffle_poker(array):
    if len(array) != 52:
        return
    for idx in range(52):
        random_idx = r.randint(idx, 51)
        array[idx], array[random_idx] = array[random_idx], array[idx]


test_array = [i for i in range(52)]
shuffle_poker(test_array)
print(test_array)


def get_random_in_flow(input, time):
    if r.randint(0, time) == 0:
        global random_element
        random_element = input


def get_randomk_in_flow(input, time, k, random_k):
    if time < k:
        random_k.append(input)
    else:
        random_idx = r.randint(0, time)
        if random_idx < k:
            random_k[random_idx] = input


test_flow1 = [1, 3, 9, 5, 2, 7, 12, 21, 8, 6]
random_element = None
for index, value in enumerate(test_flow1):
    get_random_in_flow(value, index)
    print(random_element, end=' ')
print()

k = 3
random_k = []
for index in range(len(test_flow1)):
    get_randomk_in_flow(test_flow1[index], index, k, random_k)
    print(random_k, end=' ')
print()


def random_largest(input, time):
    global largest,counter, largest_idx
    if input == largest:
        counter += 1
        if r.randint(1, counter) == 1:
            largest_idx = time
    elif input > largest:
        largest = input
        counter = 1
        largest_idx = time


largest_idx = -1
counter = 0
largest = float("-inf")
test_flow2 = [1, 3, 9, 5, 2, 3, 9, 2, 9, 2]
for index, value in enumerate(test_flow2):
    random_largest(value, index)
    print(largest_idx, end=' ')
print()


def random_5():
    result = r.randint(0, 6)
    while result >= 5:
        result = r.randint(0, 6)
    return result


def random_7():
    result = 0
    for i in range(2):
        result = result * 5 + r.randint(0, 4)
    while result >= (25 // 7 * 7):
        result = 0
        for i in range(2):
            result = result * 5 + r.randint(0, 4)
    return result % 7


for i in range(10):
    print(random_5(), end=' ')
print("random 5 based on random 7")
for i in range(10):
    print(random_7(), end=' ')
print("random 7 based on random 5")


def get_median(input, small_heap, big_heap):
    if len(small_heap) == len(big_heap):
        if not small_heap or input <= big_heap[0]:
            hq.heappush(small_heap, -input)
        else:
            hq.heappush(small_heap, -1 * hq.heappop(big_heap))
            hq.heappush(big_heap, input)
    else:
        if input >= -1 * small_heap[0]:
            hq.heappush(big_heap, input)
        else:
            hq.heappush(big_heap, -1 * hq.heappop(small_heap))
            hq.heappush(small_heap, -input)
    if len(small_heap) == len(big_heap):
        return (big_heap[0] - small_heap[0]) / 2
    return -1 * small_heap[0]


s_heap = []
b_heap = []
for element in test_flow2:
    print(get_median(element, s_heap, b_heap), end=' ')
print()