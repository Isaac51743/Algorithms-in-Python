#6/28/2020
# assuming array is not None and has >= 1 element

#helper is a assistant array with the same length of original array
def mergeSort(array, startIndex, endIndex, helper):
    if startIndex == endIndex:
        return
    midIndex = startIndex + (endIndex - startIndex)//2
    mergeSort(array, startIndex, midIndex, helper)
    mergeSort(array, midIndex + 1, endIndex, helper)
    merge(array, startIndex, midIndex, endIndex, helper)
def merge(array, startIndex, midIndex, endIndex, helper):
    # copy step
    for index in range(startIndex, endIndex + 1):
        helper[index] = array[index]
    # compare and merge step
    indexOfSubarray1 = startIndex
    indexOfSubarray2 = midIndex + 1
    while indexOfSubarray1 <= midIndex and indexOfSubarray2 <= endIndex:
        if helper[indexOfSubarray1] < helper[indexOfSubarray2]:
            array[startIndex] = helper[indexOfSubarray1]
            indexOfSubarray1 += 1
        else:
            array[startIndex] = helper[indexOfSubarray2]
            indexOfSubarray2 += 1
        startIndex += 1
    # if indexOfSubarray1 haven't arrive midIndex
    while indexOfSubarray1 <= midIndex:
        array[startIndex] = helper[indexOfSubarray1]
        indexOfSubarray1 += 1
        startIndex += 1
    # if indexOfSubarray2 haven't arrive endIndex, no operation needed

# reversive mergeSort
# array must be even
def reversiveMergeSort(array, leftIndex, rightIndex, helper):
    arrayLength = rightIndex - leftIndex + 1
    if arrayLength < 4:
        return
    startOfSubarray3 = leftIndex + arrayLength // 2
    shorterSubarrayLength = arrayLength // 4
    startOfSubarray2 = leftIndex + shorterSubarrayLength
    startOfSubarray4 = startOfSubarray3 + shorterSubarrayLength
    # swap subarray2 and subarray3
    helper[startOfSubarray2:startOfSubarray4] = array[startOfSubarray3:startOfSubarray4] + array[startOfSubarray2:startOfSubarray3]
    array[startOfSubarray2: startOfSubarray4] = helper[startOfSubarray2:startOfSubarray4]
    reversiveMergeSort(array, leftIndex, leftIndex + 2 * shorterSubarrayLength - 1, helper)
    reversiveMergeSort(array, leftIndex + 2 * shorterSubarrayLength, rightIndex, helper)

original1 = [1, 2, 4, 5, 3, 5, 7, 2, 0, 9, 6]
helper1 = [0] * len(original1)
mergeSort(original1, 0, len(original1) - 1, helper1)
print(original1)

original2 = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
helper2 = [0] * len(original2)
reversiveMergeSort(original2, 0, len(original2) - 1, helper2)
print(original2)
