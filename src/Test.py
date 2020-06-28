def selection(l):
    if len(l) == 0:
        return l
    for i in range(len(l) - 1):
        min = i
        for j in range(i, len(l)):
            if l[min] > l[j]:
                min = j
        l[i], l[min] = l[min], l[i]
    return l
def mergesort(lis, left, right):
    if len(lis) <= 1:
        return lis
    if left == right:
        return [lis[left]]
    mid =  left + (right - left)//2
    leftside = mergesort(lis, left, mid)
    rightside = mergesort(lis, mid + 1, right)
    result = merge(leftside, rightside)
    return result
def merge(l, r):
    if len(l) == 0 and len(r) == 0:
        return None
    elif len(l) == 0:
        return r
    elif len(r) == 0:
        return l
    else:
        result = []
        i = j = 0
        while len(result) < len(l) + len(r):
            if i < len(l) and j < len(r):
                if l[i] < r[j]:
                    result.append(l[i])
                    i += 1
                else:
                    result.append(r[j])
                    j += 1
            elif i == len(l):
                result.extend(r[j:])
            elif j == len(r):
                result.extend(l[i:])
        return result
def consecutive(num):
    count = 0
    for length in range(1, num + 1):
        if (num * 2) % length == 0:
            a1 = num * 2 / length - length - 1
            if a1 % 2 == 0 and a1 > 0:
                count += 1
    return count


print([1] + [2])
t = [1, 4, 6,2, 6, 2, 78, 8, 9, 10, 1, 3]
print(mergesort(t, 0, len(t) - 1))
print(ord('a'))
print(bin(256))
print(consecutive(15))
for i, j in enumerate(t):
    print([i, j])
test1 = [0] * 3
test2 = [[0]*3 for _ in range(3)]
c = 0
print()

for i in range(3):
    for j in range(3):
        c += 1
        test2[i][j] = c
        print([i, j, test2])
        j += 1
    i += 1
for i in range(1, 4):
    print('haha')
a = b = [[0, 0], [1, 1]]
b[1][0] = 0
print([1] + [2])
print(a)
print(test2)
print(min(test2))
test3 = {1:22, 2:12}
print(max(test3))
class test():
    class_variable = 'haha'
    # def __init__(self):
        # self.class_variable = 'wawa'
a = test()
print(a.class_variable)
def bridge(time):
    M = [time[0], time[1], time[0] + time[1] + time[2]]
    for i in range(3, len(time)):
        temtime1 = time[1] + time[0] + time[i] + time[1] + M[i - 2]
        temtime2 = time[0] + time[i] + M[i - 1]
        if temtime1 < temtime2:
            M.append(temtime1)
        else:
            M.append(temtime2)
    print(M)
    return M[-1]
t = [1, 2, 5, 10]
print(bridge(t))
# [1, 20, 42, 161, 184, 304]
# [1, 20, 42, 143, 245, 348]