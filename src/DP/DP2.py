def match(str1, str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)

    M = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    # basecase
    for row in range(len(str1) + 1):
        M[row][0] = row
    for col in range(len(str2) + 1):
        M[0][col] = col
    # induction rule
    for row in range(1, len(str1) + 1):
        for col in range(1, len(str2) + 1):
            if str1[row - 1] == str2[col - 1]:
                M[row][col] = M[row - 1][col - 1]
            else:
                M[row][col] = 1 + min(M[row - 1][col - 1], M[row - 1][col], M[row][col - 1])
    return M[len(str1)][len(str2)]
def largestsqua(matri):
    M = matri
    maxbound = 0
    for row in range(1, len(M)):
        for col in range(1, len(M[0])):
            if matri[row][col] == 0:
                M[row][col] = 0
            else:
                M[row][col] = 1 + min(M[row - 1][col - 1], M[row - 1][col], M[row][col - 1])
                if maxbound < M[row][col]:
                    maxbound = M[row][col]
    print(M)
    return maxbound


test1 = 'zhaoyuehang'
test2 = 'zhoyuehang'
print(match(test1, test2))
# --------------------------------------------------------------------------
edge = 6
matri = [[0] * edge for _ in range(edge)]
for i in range(2, 5):
    for j in range(2, 5):
        matri[i][j] = 1
matri[0][0] = 1
matri[1][5] = 1
print(largestsqua(matri))

