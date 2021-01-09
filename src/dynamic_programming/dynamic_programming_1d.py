import time


def time_record(func):
    def wrapper(*args):
        time1 = time.time()
        result = func(*args)
        time2 = time.time()
        print(time2 - time1)
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


def max_length_of_ascending_subarray(array):
    if len(array) == 0:
        return 0
    result = [1]
    global_max_length = result[0]
    for index in range(1, len(array)):
        if array[index] > array[index - 1]:
            result.append(result[-1] + 1)
            if result[-1] > global_max_length:
                global_max_length = result[-1]
        else:
            result.append(1)
    return global_max_length


test_array = [7, 2, 3, 1, 5, 8, 9, 6]
print(max_length_of_ascending_subarray(test_array))


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
print(max_product_of_rope1(100))
print(max_product_of_rope2(100))
print(max_product_of_rope_recursion(10))


def jumpToTheEnd(jumpSteps):
    if len(jumpSteps) <= 1:
        return True
    result = [True]
    for curIndex in range(1, len(jumpSteps)):
        canBeReach = False
        for previousIndex in range(curIndex):
            if result[previousIndex] and jumpSteps[previousIndex] >= curIndex - previousIndex:
                canBeReach = True
                break
        result.append(canBeReach)
    return result[-1]

def jumpToTheEndReverse(reversedJumpSteps):
    if len(reversedJumpSteps) <= 1:
        return True
    result = [True]
    for curIndex in range(1, len(reversedJumpSteps)):
        canJumpToTheEnd = False
        reviewRange = min(reversedJumpSteps[curIndex], curIndex)
        for preIndex in range(curIndex - reviewRange, curIndex):
            if result[preIndex] == True:
                canJumpToTheEnd = True
                break
        result.append(canJumpToTheEnd)
    return result[-1]

def minJumpToTheEndReverse(reversedJumpSteps):
    if len(reversedJumpSteps) <= 1:
        return 0
    result = [0]
    for curIndex in range(1, len(reversedJumpSteps)):
        minJumpsToTheEnd = None
        reviewRange = min(curIndex, reversedJumpSteps[curIndex])
        for preIndex in range(curIndex - reviewRange, curIndex):
            if result[preIndex] != None:
                if minJumpsToTheEnd == None or minJumpsToTheEnd > result[preIndex] + 1:
                    minJumpsToTheEnd = result[preIndex] + 1
        result.append(minJumpsToTheEnd)
    return result[-1]

print('jump to the end:')
testJump = [2, 1, 3, 2, 4, 2]
print(jumpToTheEnd(testJump))
testJump.reverse()
print(jumpToTheEndReverse(testJump))
print(minJumpToTheEndReverse(testJump))
# -----------------------------------------------------------------------------------
def largestSumOfSubarray(array):
    if len(array) == 0:
        return 0
    result = [array[0]]
    globalMaxSum = array[0]
    finalLeftIndex = finalRightIndex = temporaryLeftIndex = 0
    for index in range(1, len(array)):
        if result[-1] > 0:
            result.append(result[index - 1] + array[index])
        else:
            result.append(array[index])
            temporaryLeftIndex = index
        if globalMaxSum < result[-1]:
            globalMaxSum = result[-1]
            finalLeftIndex = temporaryLeftIndex
            finalRightIndex = index
    return (globalMaxSum, (finalLeftIndex, finalRightIndex))

testList = [1, 2, 3, -1, -20, 1, -4]
print(largestSumOfSubarray(testList))
# -----------------------------------------------------------------------------------
def canBeComposedWithConcatenatingWordsInDictionary(text, dictionary):
    if len(text) == 0:
        return True
    result = [text[0] in dictionary]
    for index in range(1, len(text)):
        canBeComposed = False
        for indexOfLeftEnd in range(index):
            if result[indexOfLeftEnd] and text[indexOfLeftEnd + 1:index + 1] in dictionary:
                canBeComposed = True
                break
        if text[:index + 1] in dictionary:
            canBeComposed = True
        result.append(canBeComposed)
    return result[-1]

dictionary = {'bob', 'cat', 'rob'}
testText = 'bobcatrob'
print(canBeComposedWithConcatenatingWordsInDictionary(testText, dictionary))
