def findLongestContiguous1(zeroOneArray):
    if len(zeroOneArray) == 0:
        return None
    result = [zeroOneArray[0]]
    finalLeft = finalRight = 0
    temporaryLeft = 0 if zeroOneArray[0] == 1 else 1
    longestLength = zeroOneArray[0]
    for index in range(1, len(zeroOneArray)):
        if zeroOneArray[index] == 1:
            result.append(result[-1] + 1)
        else:
            result.append(0)
            temporaryLeft = index + 1
        if result[-1] > longestLength:
            longestLength = result[-1]
            finalLeft = temporaryLeft
            finalRight = index
    return (longestLength, finalLeft, finalRight)

testArray1 = [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0 ,0, 0]
print(findLongestContiguous1(testArray1))
# -----------------------------------------------------------------------------------
def maxStorageOfWater(array):
    if len(array) <= 1:
        return 0
    # find vertex
    vertex = []
    index = 0
    while True:
        # up
        while index < len(array) - 1 and array[index] <= array[index + 1]:
            index += 1
        vertex.append(index)
        if index == len(array) - 1:
            break
        # down
        while index < len(array) - 1 and array[index] > array[index + 1]:
            index += 1
        if index == len(array) - 1:
            break
    if len(vertex) <= 1:
        return 0
    print(vertex)
    # find vertex in vertex
    vertexOfVertex = []
    index = 0
    while True:
        while index < len(vertex) - 1 and array[index] <= array[index + 1]:
            index += 1
        vertexOfVertex.append(index)
        if index == len(vertex) - 1:
            break
        while index < len(vertex) - 1 and array[index] > array[index + 1]:
            index += 1
        if index == len(vertex) - 1:
            break
    print(vertexOfVertex)
    if len(vertexOfVertex) > 1:
        newVertex = []
        for index in range(vertexOfVertex[0]):
            newVertex.append(vertex[index])
        for index in vertexOfVertex:
            newVertex.append(vertex[index])
        for index in range(vertexOfVertex[-1] + 1, len(vertex)):
            newVertex.append(vertex[index])
    else:
        newVertex = vertex
    storage = 0
    for leftBound in range(len(newVertex) - 1):
        for index in range(newVertex[leftBound] + 1, newVertex[leftBound + 1]):
            if array[index] < min(array[newVertex[leftBound]], array[newVertex[leftBound + 1]]):
                storage += min(array[newVertex[leftBound]], array[newVertex[leftBound + 1]]) - array[index]
    return storage

fence1 = [5, -1, 2, -1, 5, 5]
print(maxStorageOfWater(fence1))
# -----------------------------------------------------------------------------------
def matrixPrint(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            print(matrix[row][column], end=' ')
        print()

def findLargestCross(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    leftArm = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    rightArm = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    topArm = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    downArm = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for index1 in range(len(matrix)):
        row = index1
        leftArm[row][0] = matrix[row][0]
        for index2 in range(1, len(matrix[0])):
            column = index2
            if matrix[row][column] == 0:
                leftArm[row][column] = 0
            else:
                leftArm[row][column] = leftArm[row][column - 1] + 1
    for index1 in range(len(matrix)):
        row = index1
        leftArm[row][len(matrix[0]) - 1] = matrix[row][len(matrix[0]) - 1]
        for index2 in range(1, len(matrix[0])):
            column = len(matrix[0]) - 1 - index2
            if matrix[row][column] == 0:
                rightArm[row][column] = 0
            else:
                rightArm[row][column] = rightArm[row][column + 1] + 1
    for index1 in range(len(matrix[0])):
        column = index1
        topArm[0][column] = matrix[0][column]
        for index2 in range(1, len(matrix)):
            row = index2
            if matrix[row][column] == 0:
                topArm[row][column] = 0
            else:
                topArm[row][column] = topArm[row - 1][column] + 1
    for index1 in range(len(matrix[0])):
        column = index1
        downArm[len(matrix) - 1][column] = matrix[len(matrix) - 1][column]
        for index2 in range(1, len(matrix)):
            row = len(matrix) - 1 - index2
            if matrix[row][column] == 0:
                downArm[row][column] = 0
            else:
                downArm[row][column] = downArm[row + 1][column] + 1
    globalMaxArmLength = -1
    finalRow = finalColumn = -1
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            minArm = min(leftArm[row][column], rightArm[row][column], topArm[row][column], downArm[row][column]) - 1
            if globalMaxArmLength < minArm:
                globalMaxArmLength = minArm
                finalRow = row
                finalColumn = column
    return (globalMaxArmLength, finalRow, finalColumn)

testMatrix1 = [[0 for _ in range(10)] for _ in range(10)]
for row in range(5):
    testMatrix1[row][5//2] = 1
for column in range(5):
    testMatrix1[5//2][column] = 1
matrixPrint(testMatrix1)
print(findLargestCross(testMatrix1))
# -----------------------------------------------------------------------------------
def findLargestSquareSurroundedByOne(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    leftToRight = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    rightToLeft = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    topToBottom = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    bottomToTop = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    # topLeftCorner = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    # bottomRightCorner = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for index1 in range(len(matrix)):
        row = index1
        leftToRight[row][0] = matrix[row][0]
        for index2 in range(1, len(matrix[0])):
            column = index2
            if matrix[row][column] == 0:
                leftToRight[row][column] = 0
            else:
                leftToRight[row][column] = leftToRight[row][column - 1] + 1
    for index1 in range(len(matrix)):
        row = index1
        rightToLeft[row][len(matrix[0]) - 1] = matrix[row][len(matrix[0]) - 1]
        for index2 in range(1, len(matrix[0])):
            column = len(matrix[0]) - 1 - index2
            if matrix[row][column] == 0:
                rightToLeft[row][column] = 0
            else:
                rightToLeft[row][column] = rightToLeft[row][column + 1] + 1
    for index1 in range(len(matrix[0])):
        column = index1
        topToBottom[0][column] = matrix[0][column]
        for index2 in range(1, len(matrix)):
            row = index2
            if matrix[row][column] == 0:
                topToBottom[row][column] = 0
            else:
                topToBottom[row][column] = topToBottom[row - 1][column] + 1
    for index1 in range(len(matrix[0])):
        column = index1
        bottomToTop[len(matrix) - 1][column] = matrix[len(matrix) - 1][column]
        for index2 in range(1, len(matrix)):
            row = len(matrix) - 1 - index2
            if matrix[row][column] == 0:
                bottomToTop[row][column] = 0
            else:
                bottomToTop[row][column] = bottomToTop[row + 1][column] + 1
    globalMaxEdgeLength = 0
    finalRow = finalColumn = -1
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            lengthOfTopLeftEdges = min(rightToLeft[row][column], bottomToTop[row][column])
            for i in range(lengthOfTopLeftEdges):
                edgeLength = lengthOfTopLeftEdges - i
                rowOfBottomRightCorner = row + edgeLength - 1
                columnOfBottomRightCorner = column + edgeLength - 1
                if rowOfBottomRightCorner < len(matrix) and columnOfBottomRightCorner < len(matrix[0]):
                    bottomRightEdgeLength = min(leftToRight[rowOfBottomRightCorner][columnOfBottomRightCorner], topToBottom[rowOfBottomRightCorner][columnOfBottomRightCorner])
                    if bottomRightEdgeLength >= edgeLength and edgeLength > globalMaxEdgeLength:
                        globalMaxEdgeLength = edgeLength
                        finalRow = row
                        finalColumn = column
                        break
    return (globalMaxEdgeLength, finalRow, finalColumn)

testMatrix2 = [[0 for _ in range(10)] for _ in range(10)]
for i in range(4):
    testMatrix2[1][1 + i] = 1
for i in range(4):
    testMatrix2[4][1 + i] = 1
for i in range(4):
    testMatrix2[1 + i][1] = 1
for i in range(4):
    testMatrix2[1 + i][4] = 1
matrixPrint(testMatrix2)
print(findLargestSquareSurroundedByOne(testMatrix2))
# -----------------------------------------------------------------------------------
def pathPrefixOfArray(array):
    if len(array) == 0:
        return None
    for index in range(1, len(array)):
        array[index] = array[index - 1] + array[index]
    return array
def getSumOfSubarray(pathPrefixArray, leftIndex, rightIndex):
    if len(pathPrefixArray) == 0 or leftIndex > rightIndex:
        print('invalid parameter')
        return -1
    if leftIndex == 0:
        return pathPrefixArray[rightIndex]
    return pathPrefixArray[rightIndex] - pathPrefixArray[leftIndex - 1]

testArray2 = [1, 2, 4, 2, 14, 23, 5, 3]
print(getSumOfSubarray(pathPrefixOfArray(testArray2), 2, 5))
# -----------------------------------------------------------------------------------
def findLargestSumOfSubmatrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    result[0][0] = matrix[0][0]
    for column in range(1, len(matrix[0])):
        result[0][column] = result[0][column - 1] + matrix[0][column]
    for row in range(1, len(matrix)):
        result[row][0] = result[row - 1][0] + matrix[row][0]
    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[0])):
            result[row][column] = result[row - 1][column] + result[row][column - 1] - result[row - 1][column - 1] + matrix[row][column]
    maxSum = float('-inf')
    matrixPrint(result)
    print(maxSum)
    finalTopLeft = finalBottomRight = None
    for rowStart in range(len(matrix)):
        for rowEnd in range(rowStart, len(matrix)):
            for columnStart in range(len(matrix[0])):
                for columnEnd in range(columnStart, len(matrix[0])):
                    if rowStart == 0 and columnStart == 0:
                        temporarySum = result[rowEnd][columnEnd]
                    elif rowStart == 0:
                        temporarySum = result[rowEnd][columnEnd] - result[rowEnd][columnStart - 1]
                    elif columnStart == 0:
                        temporarySum = result[rowEnd][columnEnd] - result[rowStart - 1][columnEnd]
                    else:
                        temporarySum = result[rowEnd][columnEnd] - result[rowStart - 1][columnEnd] - result[rowEnd][columnStart - 1] + result[rowStart - 1][columnStart - 1]
                    if maxSum < temporarySum:
                        maxSum = temporarySum
                        finalTopLeft = (rowStart, columnStart)
                        finalBottomRight = (columnEnd, columnEnd)
    return (maxSum, finalTopLeft, finalBottomRight)

testMatrix3 = [[1, 1, 1, -100, 2, 1, 1, 1, 1, 1], \
                        [1, 1, 1, 1, 1, 1, 1, 1, 99, 1], \
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
                        [1, 1, 1, 1, 1, 1, 1, 2, 1, 1], \
                        [1, 1, 1,  -100, 1, 1, 1, 1, 1, 1], \
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
                        [1, 1, 1,  -100, 1, 1, 1, 1, 1, 1]]
print(findLargestSumOfSubmatrix(testMatrix3))

