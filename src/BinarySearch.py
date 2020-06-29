# 6/28/2020
# assuming array is not None and len(array) >= 1
def binarySearchRecursion(array, startIndex, endIndex, target):
    if startIndex > endIndex:
        return -1
    midIndex = startIndex + (endIndex - startIndex) // 2
    if array[midIndex] < target:
        return binarySearchRecursion(array, midIndex + 1, endIndex, target)
    elif array[midIndex] > target:
        return binarySearchRecursion(array, startIndex, midIndex - 1, target)
    else:
        return midIndex

def binarySearchIteration(array, target):
    if array == None or len(array) == 0:
        return -1
    leftIndex = 0
    rightIndex = len(array) - 1
    while leftIndex <= rightIndex:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        if array[midIndex] < target:
            leftIndex = midIndex + 1
        elif array[midIndex] > target:
            rightIndex = midIndex - 1
        else:
            return midIndex
    return -1

def binarySearch2DIteration(matrix, target):
    if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    rowNum = len(matrix)
    columnNum = len(matrix[0])
    leftIndex = 0
    rightIndex = rowNum * columnNum
    while leftIndex <= rightIndex:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        if matrix[midIndex // columnNum][midIndex % columnNum] > target:
            rightIndex = midIndex - 1
        elif matrix[midIndex // columnNum][midIndex % columnNum] < target:
            leftIndex = midIndex + 1
        else:
            return [midIndex // columnNum, midIndex % columnNum]
    return None

def binarySearch2DRecursion(matrix, target, leftIndex, rightIndex, columnNum):
    if leftIndex > rightIndex:
        return None
    midIndex = leftIndex + (rightIndex - leftIndex) // 2
    if matrix[midIndex // columnNum][midIndex % columnNum] > target:
        rightIndex = midIndex - 1
    elif matrix[midIndex // columnNum][midIndex % columnNum] < target:
        leftIndex = midIndex + 1
    else:
        return [midIndex // columnNum, midIndex % columnNum]
    return binarySearch2DRecursion(matrix, target, leftIndex, rightIndex, columnNum)

def binarySearchClosetIndex1(array, target):
    if array == None or len(array) == 0:
        return -1
    leftIndex = 0
    rightIndex = len(array) - 1
    while leftIndex < rightIndex - 1:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        if array[midIndex] > target:
            rightIndex = midIndex
        elif array[midIndex] < target:
            leftIndex = midIndex
        else:
            return midIndex
    # post processing
    if abs(target - array[leftIndex]) <= abs(target - array[rightIndex]):
        return leftIndex
    else:
        return rightIndex

def binarySearchClosetIndex2(array, target):
    if array == None or len(array) == 0:
        return -1
    leftIndex = 0
    rightIndex = len(array) - 1
    closetIndex = 0
    while leftIndex <= rightIndex:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        if abs(target - array[midIndex]) < abs(target - array[closetIndex]):
            closetIndex = midIndex
        if array[midIndex] > target:
            rightIndex = midIndex - 1
        elif array[midIndex] < target:
            leftIndex = midIndex + 1
        else:
            return midIndex
    return closetIndex

def binarySearchFirstOccurIndex1(array, target):
    if array == None or len(array) == 0:
        return -1
    leftIndex = 0
    rightIndex = len(array) - 1
    while leftIndex < rightIndex - 1:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        if array[midIndex] > target:
            rightIndex = midIndex - 1
        elif array[midIndex] < target:
            leftIndex = midIndex + 1
        else:
            rightIndex = midIndex
    # post processing
    if array[leftIndex] == target:
        return leftIndex
    elif array[rightIndex] == target:
        return rightIndex
    else:
        return -1

def binarySearchFirstOccurIndex2(array, target):
    if array == None or len(array) == 0:
        return -1
    leftIndex = 0
    rightIndex = len(array) - 1
    while leftIndex <= rightIndex:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        if array[midIndex] > target:
            rightIndex = midIndex - 1
        elif array[midIndex] < target:
            leftIndex = midIndex + 1
        else:
            if midIndex > 0 and array[midIndex - 1] == target:
                rightIndex = midIndex - 1
            else:
                return midIndex
    return -1

# assuming keys in dictionary in consecutive starting from 1, values are in ascending order
# assuming the dictionary at least has 1 key:value pair
def searchInUnknownSizeDictionary(dictionary, target):
    if dictionary == None:
        return None
    leftIndex = 1
    rightIndex = 1
    while rightIndex in dictionary and dictionary[rightIndex] < target:
        leftIndex = rightIndex + 1
        rightIndex = rightIndex * 2
    while leftIndex <= rightIndex:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        if midIndex in dictionary:
            if dictionary[midIndex] < target:
                leftIndex = midIndex + 1
            elif dictionary[midIndex] > target:
                rightIndex = midIndex - 1
            else:
                return midIndex
        else:
            rightIndex = midIndex - 1
    return -1

def binarySearchLargestSmallerEqual(array, target):
    if array == None or len(array) == 0:
        return None
    leftIndex = 0
    rightIndex = len(array) - 1
    while leftIndex < rightIndex - 1:
        midIndex = leftIndex + (rightIndex - leftIndex) // 2
        if array[midIndex] < target:
            leftIndex = midIndex
        elif target < array[midIndex]:
            rightIndex = midIndex - 1
        else:
            return midIndex
    if array[rightIndex] <= target:
        return rightIndex
    else:
        return leftIndex

original =[2, 4, 6, 8, 9, 14, 14, 16, 17, 25, 27, 34, 56]
print(binarySearchRecursion(original, 0, len(original) - 1, 6))
print(binarySearchClosetIndex2(original, 10))
print(binarySearchFirstOccurIndex1(original, 14))
print(binarySearchFirstOccurIndex2(original, 14))
print(binarySearchLargestSmallerEqual(original, 10))

matrix = [[1, 4, 6], [8, 9, 12], [24, 35, 67]]
print(binarySearch2DIteration(matrix, 67))
print(binarySearch2DRecursion(matrix, 67, 0, len(matrix) * len(matrix[0]) - 1, len(matrix[0])))

dictionary = {1: 2, 2: 4, 3: 5, 4 : 8, 5: 10, 6: 19}
print(searchInUnknownSizeDictionary(dictionary, 10))
