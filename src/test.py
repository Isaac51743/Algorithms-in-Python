def consecutive(num):
    count = 0
    for length in range(1, num + 1):
        if (num * 2) % length == 0:
            a1 = num * 2 / length - length - 1
            if a1 % 2 == 0 and a1 > 0:
                count += 1
    return count


test3 = {1:22, 2:12}
print(max(test3))

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

print('haha')

from queue import Queue
a = Queue(10)
from collections import defaultdict
b = {}
for i in range(10):
    b[i] = set()
    print(i, b[i])
print(b)
print(b[1])
del b[1]
print(int(-3/2))
from queue import PriorityQueue as pq
c = pq()
c.put(1)
from collections import deque
d = deque([])
print('zhaoyu ehag'.split())
for i in range(0, 0):
    print('sd')
import math
print(set(t))
s = sorted(t)
print(1 >> 5)
def threeAndFive(num, result):
    if num > 10 ** 2:
        return
    result.append(num)
    threeAndFive(num * 3, result)
    threeAndFive(num * 5, result)
result = []
threeAndFive(3, result)
threeAndFive(5, result)
print(result)

from math import sin, radians
print(sin(radians(90)))
a = ['1:a:b:c', '1:ab:b:c']
a.sort()
print(not [])
a = open('/Users/yuehangzhao/Downloads/resume/akuna/regular knowledge.docx')
print(a)