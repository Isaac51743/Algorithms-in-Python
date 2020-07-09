def minimumStepTotransform(text1, text2):
    if len(text1) == 0:
        return len(text2)
    elif len(text2) == 0:
        return len(text1)
    result = [[0 for i in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
    for column in range(len(result[0])):
        result[0][column] = column
    for row in range(len(result)):
        result[row][0] = row
    for row in range(1, len(text2) + 1):
        for column in range(1, len(text1) + 1):
            if text1[column - 1] ==text2[row - 1]:
                result[row][column] = result[row - 1][column - 1]
            else:
                minimumStep = min(result[row][column - 1], result[row - 1][column], result[row - 1][column - 1])
                result[row][column] = minimumStep + 1
    return result[len(text2)][len(text1)]

testText1 = 'zhaoyuehang'
testText2 = 'zhoyuehang'
print(minimumStepTotransform(testText2, testText1))

def maxLengthOfSquareOfOne(matrix):
    if len(matrix) <= 1:
        return len(matrix)
    elif len(matrix[0]) <= 1:
        return len(matrix[0])
    result = matrix
    # result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    # for row in range(len(matrix)):
    #     result[row][0] = matrix[row][0]
    # for column in range(len(matrix[0])):
    #     result[0][column] = matrix[0][column]
    maxLength = 0
    for row in range(1, len(matrix)):
        for column in range(1, len(matrix[0])):
            if matrix[row][column] == 1:
                result[row][column] = min(result[row - 1][column - 1], result[row][column - 1], result[row - 1][column]) + 1
                if result[row][column] > maxLength:
                    maxLength = result[row][column]
            else:
                result[row][column] = 0
    return maxLength

edgeLength = 6
testMatrix = [[0] * edgeLength for _ in range(edgeLength)]
for i in range(2, 5):
    for j in range(2, 5):
        testMatrix[i][j] = 1
testMatrix[0][0] = 1
testMatrix[1][5] = 1
print(maxLengthOfSquareOfOne(testMatrix))

