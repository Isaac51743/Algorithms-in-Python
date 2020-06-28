def larsum(array):
    if len(array) == 0:
        return None
    M = [array[0]]
    sum = array[0]
    finalstart = finalend = start = 0
    for i in range(1, len(array)):
        if M[-1] > 0:
            M.append(M[-1] + array[i])
        else:
            M.append(array[i])
            start = i
        if M[-1] > sum:
            finalstart = start
            finalend = i
            sum = M[-1]
    print(array[finalstart:finalend + 1])
    return M[-1]
def rain(array):
    if len(array) <= 1:
        return 0
    vertex = []
    i = 0
    while 1:
        # up
        while i < len(array) - 1 and array[i + 1] > array[i]:
            i += 1
        vertex.append(i)
        if i == len(array) - 1:
            break
        # down
        while i < len(array) - 1 and array[i + 1] < array[i]:
            i += 1
        if i == len(array) - 1:
            break
    if len(vertex) <= 1:
        return 0
    sum = 0
    for i in range(len(vertex) - 1):
        # vertex[i] to vertex[i + 1]
        for j in range(vertex[i] + 1, vertex[i + 1]):
            if array[j] < min(array[vertex[i]], array[vertex[i + 1]]):
                sum += min(array[vertex[i]], array[vertex[i + 1]]) - array[j]
                # print(min(array[vertex[i]], array[vertex[i + 1]]) - array[j], end=' ')
        # print()
    return sum
def conti1(array):
    if len(array) == 0:
        return 0
    longest = array[0]
    finalleft = finalright = start = 0
    M = []
    for i in range(1, len(array)):
        if array[i] == 1:
            M.append(M[-1] + 1)
        else:
            M.append(0)
            start = i + 1
        if M[-1] > longest:
            longest = M[-1]
            finalright = i
            finalleft = start
    return [longest, finalleft, finalright]
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


test = [1, -2, 3, 1, 4, 5, -12, 40]
print(larsum(test))
print(rain(test))
test1 = [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0 ,0, 0]
print(conti1(test1))
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
