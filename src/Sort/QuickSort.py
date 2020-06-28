# 6/28/2020
def quickSort(array, startIndex, endIndex):
    if startIndex >= endIndex:
        return
    startOfUnsorted = startIndex
    endOfUnsorted = endIndex - 1
    while startOfUnsorted <= endOfUnsorted:
        if array[startOfUnsorted] < array[endIndex]:
            startOfUnsorted += 1
        else:
            array[startOfUnsorted], array[endOfUnsorted] = array[endOfUnsorted], array[startOfUnsorted]
            endOfUnsorted -= 1
    array[startOfUnsorted], array[endIndex] = array[endIndex], array[startOfUnsorted]
    quickSort(array, startIndex, startOfUnsorted - 1)
    quickSort(array, startOfUnsorted + 1, endIndex)

original = [1, 4, 6, 7, 3, 45, 8, 3, 7, 4, 8, 68, 23]
quickSort(original, 0, len(original) - 1)
print(original)