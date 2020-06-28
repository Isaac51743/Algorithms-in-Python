def fibonacci(n):
    dic = {}
    dic[0] = 0
    dic[1] = 1
    for i in range(2, n + 1):
        dic[i] = dic[i - 1] + dic[i - 2]
    return dic[n]

def maxascendingsubarray(array):
    if len(array) == 0:
        return None
    globalmax = 1
    maxlength = [1]
    for i in range(1, len(array)):
        if array[i] >= array[i - 1]:
            maxlength.append(maxlength[-1] + 1)
        else:
            maxlength.append(1)
        if maxlength[-1] > globalmax:
            globalmax = maxlength[-1]
    return globalmax

def maxproduct(n):
    maxpro = [-1, -1]
    for length in range(2, n + 1):
        temmax = 0
        for left in range(1, length//2 + 1):
            temmax = max(temmax, max(left, maxpro[left]) * max(length - left, maxpro[length - left]))
        maxpro.append(temmax)
    return maxpro[-1]
def maxproduct1(n):
    maxpro = [0, 0]
    for length in range(2, n + 1):
        temmax = 0
        for left in range(1, length):
            temmax = max(temmax, left * max(length - left, maxproduct1(length - left)))
        maxpro.append(temmax)
    return maxpro[-1]
def maxproduct2(n):
    if n <= 1:
        return 0
    temmax = 0
    for left in range(1, n):
        temmax = max(temmax, max(left, maxproduct2(left)) * max(n - left, maxproduct2(n - left)))
    return temmax
def reverse(array):
    if len(array) <= 1:
        return array
    l = 0
    r = len(array) - 1
    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1
    # return array
def jumpgame(array):
    if len(array) <= 1:
        return True
    # reverse(array)
    # print(array)
    record = [True]
    for i in range(1, len(array)):
        review = min(array[i], i ) # number of previous elements we can review
        for j in range(i - review, i):
            if record[j] == True:
                record.append(True)
                break
        if len(record) == i:
            record.append(False)
    return record[-1]
def minjump(array):
    if len(array) == 0:
        return None
    # reverse(array)
    record = [0]
    for i in range(1, len(array)):
        review = min(i, array[i])
        temjumps = len(array)   # max jumps we can make
        for j in range(i - review, i):
            if record[j] != None and record[j] < temjumps:
                temjumps = record[j]
        if temjumps == len(array):
            record.append(None)
        else:
            record.append(temjumps + 1)
    return record[-1]
def larsumsubarray(array):
    if len(array) == 0:
        return None
    record = [array[0]]
    maxsum = array[0]
    finall = finalr = l = 0
    for i in range(1, len(array)):
        if record[-1] > 0:
            record.append(array[i] + record[-1])
        else:
            record.append(array[i])
            l = i
        if maxsum < record[-1]:
            maxsum = record[-1]
            finall = l
            finalr = i
    print(record)
    return [maxsum, array[finall:finalr + 1]]
def dictionaryword(st, dic):
    if len(st) == 0:
        return False
    record = [st[0] in dic]
    for idx in range(1, len(st)):
        if st[: idx + 1] in dic:
            record.append(True)
            continue
        record.append(False)
        for left in range(idx):
            if record[left] and (st[left + 1:idx + 1] in dic):
                record[-1] = True
                break
    return record[-1]


print(fibonacci(64))
test = [7, 2, 3, 1, 5, 8, 9, 6]
print(maxascendingsubarray(test))
print(maxproduct1(10))
jump = [2, 1, 3, 2, 4, 2]
reverse(jump)
print(jumpgame(jump))
print(minjump(jump))
test1 = [1, 2, 3, -1, -20, 1, -4]
print(larsumsubarray(test1))
dic = {'bob', 'cat', 'rob'}
st = 'bobcatrob'
print(dictionaryword(st, dic))
