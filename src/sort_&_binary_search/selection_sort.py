# 06/28/2020


def selectionSort(array):
    if array == None or len(array) == 0:
        return array
    arrayLength = len(array)
    for startOfUnsortedSubarray in range(arrayLength - 1):
        indexOfMin = startOfUnsortedSubarray
        for index in range(startOfUnsortedSubarray + 1, arrayLength):
            if array[index] < array[indexOfMin]:
                indexOfMin = index
        array[startOfUnsortedSubarray], array[indexOfMin] = array[indexOfMin], array[startOfUnsortedSubarray]
    return array

unsortedArray = [-2, 5, 7, 3, 6]
sortedArray = selectionSort(unsortedArray)
print(sortedArray)
