def fibonacci(n):
    result = []
    for i in range(n + 1):
        if i <= 1:
            result.append(i)
        else:
            result.append(result[i - 1] + result[i - 2])
    return result[-1]
print(fibonacci(9))

def maxLengthOfAscendingSubarray(array):
    if len(array) == 0:
        return 0
    result = [1]
    globalMaxLength = result[0]
    for index in range(1, len(array)):
        if array[index] > array[index - 1]:
            result.append(result[-1] + 1)
            if result[-1] > globalMaxLength:
                globalMaxLength = result[-1]
        else:
            result.append(1)
    return globalMaxLength

testArray = [7, 2, 3, 1, 5, 8, 9, 6]
print(maxLengthOfAscendingSubarray(testArray))

def maxProductOfRope1(ropeLength):
    result = [-1, -1]
    if ropeLength <= 1:
        return result[ropeLength]
    for length in range(2, ropeLength + 1):
        maxProduct = 0
        for lengthOfShorter in range(1, length // 2 + 1):
            curProduct = max(lengthOfShorter, result[lengthOfShorter]) * max(length - lengthOfShorter, result[length - lengthOfShorter])
            maxProduct = max(maxProduct, curProduct)
        result.append(maxProduct)
    return result[-1]

def maxProductOfRope2(ropeLength):
    result = [-1, -1]
    if ropeLength <= 1:
        return result[ropeLength]
    for length in range(2, ropeLength + 1):
        maxProduct = 0
        for leftLength in range(1, length):
            curProdcut = leftLength * max(length - leftLength, result[length - leftLength])
            maxProduct = max(curProdcut, maxProduct)
        result.append(maxProduct)
    return result[-1]

def maxProductOfRopeRecursion(ropeLength):
    if ropeLength == 1:
        return -1
    maxProduct = 0
    for leftLength in range(1, ropeLength):
        curProduct = leftLength * max(ropeLength - leftLength, maxProductOfRopeRecursion(ropeLength - leftLength))
        maxProduct = max(maxProduct, curProduct)
    return maxProduct

print(maxProductOfRope2(10))
print(maxProductOfRopeRecursion(10))
# -----------------------------------------------------------------------------------
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
