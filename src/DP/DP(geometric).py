def findLongestContiguous1(zeroOneArray):
    if len(zeroOneArray) == 0:
        return 0
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

def larcross(array):
    if len(array) == 0:
        return 0
    M1 = [[0]*len(array[0]) for _ in range(len(array))]
    M2 = [[0]*len(array[0]) for _ in range(len(array))]
    M3 = [[0]*len(array[0]) for _ in range(len(array))]
    M4 = [[0]*len(array[0]) for _ in range(len(array))]
    # left to right
    for row in range(len(array)):
        M1[row][0] = array[row][0]
        for col in range(1, len(array[0])):
            if array[row][col] == 1:
                M1[row][col] = M1[row][col - 1] + 1
            else:
                M1[row][col] = 0
    # right to left
    for row in range(len(array)):
        M2[row][len(array[0]) - 1] = array[row][len(array[0]) - 1]
        for col in range(1, len(array[0])):
            if array[row][len(array[0]) - 1 - col] == 1:
                M2[row][len(array[0]) - 1 - col] = M2[row][len(array[0]) - col] + 1
            else:
                M2[row][len(array[0]) - 1 - col] = 0
    # up to down
    for col in range(len(array[0])):
        M3[0][col] = array[0][col]
        for row in range(1, len(array)):
            if array[row][col] == 1:
                M3[row][col] = M3[row - 1][col] + 1
            else:
                M3[row][col] = 0
    # down to up
    for col in range(len(array[0])):
        M4[len(array) - 1][col] = array[len(array) - 1][col]
        for row in range(1, len(array)):
            if array[len(array) - 1 - row][col] == 1:
                M4[len(array) - 1 - row][col] = M4[len(array) - row][col] + 1
            else:
                M4[len(array) - 1 - row][col] = 0
    maxarm = 0
    for row in range(len(array)):
        for col in range(len(array[0])):
            localmin = min(M1[row][col], M2[row][col], M3[row][col], M4[row][col])
            if localmin > maxarm:
                maxarm = localmin
                position = [row, col]
    # matrixprint(M4)
    return [maxarm, position]
def matrixprint(mat):
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            print(mat[r][c], end=' ')
        print()

def larsurround(array):
    if len(array) == 0:
        return 0
    M1 = [[0]*len(array[0]) for _ in range(len(array))]
    M2 = [[0]*len(array[0]) for _ in range(len(array))]
    M3 = [[0]*len(array[0]) for _ in range(len(array))]
    M4 = [[0]*len(array[0]) for _ in range(len(array))]
    # left to right
    for row in range(len(array)):
        M1[row][0] = array[row][0]
        for col in range(1, len(array[0])):
            if array[row][col] == 1:
                M1[row][col] = M1[row][col - 1] + 1
            else:
                M1[row][col] = 0
    # right to left
    for row in range(len(array)):
        M2[row][len(array[0]) - 1] = array[row][len(array[0]) - 1]
        for col in range(1, len(array[0])):
            if array[row][len(array[0]) - 1 - col] == 1:
                M2[row][len(array[0]) - 1 - col] = M2[row][len(array[0]) - col] + 1
            else:
                M2[row][len(array[0]) - 1 - col] = 0
    # up to down
    for col in range(len(array[0])):
        M3[0][col] = array[0][col]
        for row in range(1, len(array)):
            if array[row][col] == 1:
                M3[row][col] = M3[row - 1][col] + 1
            else:
                M3[row][col] = 0
    # down to up
    for col in range(len(array[0])):
        M4[len(array) - 1][col] = array[len(array) - 1][col]
        for row in range(1, len(array)):
            if array[len(array) - 1 - row][col] == 1:
                M4[len(array) - 1 - row][col] = M4[len(array) - row][col] + 1
            else:
                M4[len(array) - 1 - row][col] = 0
    maxarm = 0
    for row in range(len(array)):
        for col in range(len(array[0])):
            largestedge = min(M2[row][col], M4[row][col])
            for e in range(largestedge):
                edge = largestedge - e # edge from largest to smallest
                temr = row + edge - 1
                temc = col + edge - 1
                bottomright = min(M1[temr][temc], M3[temr][temc])
                if bottomright >= edge: # ensure a subsquare
                    if edge > maxarm:
                        maxarm = edge
                    break
    return maxarm
def quicksum(array):
    if len(array) == 0:
        return None
    M = [0] * len(array)
    M[0] = array[0]
    for i in range(1, len(array)):
        M[i] = array[i] + M[i - 1]
    return M
def sumofsubmatrix(matri):
    M = [[0] * len(matri[0]) for _ in range(len(matri))]
    M[0][0] = matri[0][0]
    for row in range(1, len(matri)):
        M[row][0] = matri[row][0] + M[row - 1][0]
    for col in range(1, len(matri[0])):
        M[0][col] = matri[0][col] + M[0][col - 1]
    for row in range(1, len(matri)):
        for col in range(1, len(matri[0])):
            M[row][col] = M[row - 1][col] + M[row][col - 1] - M[row - 1][col - 1] + matri[row][col]
    return M




# ---------------------------------------------------------------------------------
test2 = [[0] * 10 for _ in range(10)]
for r in range(5):
    test2[r][5//2] = 1
for c in range(5):
    test2[5//2][c] = 1
matrixprint(test2)
print(larcross(test2))
# ---------------------------------------------------------------------------------
test3 = [[0]*10 for _ in range(10)]
for i in range(4):
    test3[1][1 + i] = 1
for i in range(4):
    test3[4][1 + i] = 1
for i in range(4):
    test3[1 + i][1] = 1
for i in range(4):
    test3[1 + i][4] = 1
print(larsurround(test3))
# ---------------------------------------------------------------------------------
test4 = [1, 2, 4, 2, 14, 23, 5, 3]
record = quicksum(test4)
def query(record, start, end):
    if start == 0:
        return record[end]
    return record[end] - record[start - 1]
print(query(record, 2, 5))
# ---------------------------------------------------------------------------------
test5 = [[1, 1, 1, -100, 2, 1, 1, 1, 1, 1], \
            [1, 1, 1, 1, 1, 1, 1, 1, 2, 1], \
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
            [1, 1, 1, 1, 1, 1, 1, 2, 1, 1], \
            [1, 1, 1,  -100, 1, 1, 1, 1, 1, 1], \
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
            [1, 1, 1,  -100, 1, 1, 1, 1, 1, 1]]
record = sumofsubmatrix(test5)
def maxsum(M):
    maxsum = -99999999999
    for r1 in range(len(M)):
        for r2 in range(r1, len(M)):
            for c1 in range(len(M[0])):
                for c2 in range(c1, len(M[0])):
                    if r1 == 0 and c1 == 0:
                        temsum = M[r2][c2]
                    elif r1 == 0:
                        temsum = M[r2][c2] - M[r2][c1 - 1]
                    elif c1 == 0:
                        temsum = M[r2][c2] - M[r1 - 1][c2]
                    else:
                        temsum = M[r2][c2] - M[r1 - 1][c2 - 1] - M[r2 - 1][c1 - 1] + M[r1 - 1][c1 - 1]
                    if temsum > maxsum:
                        maxsum = temsum
                        result = [maxsum, (r1, c1), (r2, c2)]
    return result
matrixprint(record)
print(maxsum(record))
