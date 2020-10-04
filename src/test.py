from collections import defaultdict
from queue import Queue
from math import sin, radians
from queue import PriorityQueue as pq
import math
from collections import deque
import sys


def consecutive(num):
    count = 0
    for length in range(1, num + 1):
        if (num * 2) % length == 0:
            a1 = num * 2 / length - length - 1
            if a1 % 2 == 0 and a1 > 0:
                count += 1
    return count


def bridge(time):
    m = [time[0], time[1], time[0] + time[1] + time[2]]
    for i in range(3, len(time)):
        tem_time1 = time[1] + time[0] + time[i] + time[1] + m[i - 2]
        tem_time2 = time[0] + time[i] + m[i - 1]
        if tem_time1 < tem_time2:
            m.append(tem_time1)
        else:
            m.append(tem_time2)
    print(m)
    return m[-1]


def threeAndFive(num, result):
    if num > 10 ** 2:
        return
    result.append(num)
    threeAndFive(num * 3, result)
    threeAndFive(num * 5, result)


test3 = {1:22, 2:12}
print(max(test3))

t = [1, 2, 5, 10]
print(bridge(t))

a = Queue(10)

# defaultdict
b = defaultdict(set)
b[1].add(1)
print(b[1])

c = pq()
c.put([1, 6000])
c.put([2, 3])
print('priority queue test:', c.get())

d = deque([])
print('zhaoyu ehag'.split())
for i in range(0, 0):
    print('sd')

print(set(t))
s = sorted(t)
print(1 >> 5)

result = []
threeAndFive(3, result)
threeAndFive(5, result)
print((1, 4, 2, 10, 4))

print(sin(radians(90)))
a = ['1:a:b:c', '1:ab:b:c']
a.sort()
print(a)
print(not [])

try:
    a = open('test_file', 'w')
    a.write('haah\n')
finally:
    a.close()
with open('test_file', 'a') as a:
    a.write('zhaoyuehagn\n')
i = 2
for i in range(5):
    print(i)
print(i)

a = [[2, 1, 1], [1, 1, 0], [0, 1, 1]] * 100
print("lalaalla", sys.getsizeof(a))
b = iter(a)
print(sys.getsizeof(b))
print(max([max(_) for _ in a]))
def zhao(a):
    a = [10]
    return a
zhao(a)
print(a)

with open('output', 'w') as f:
    f.write('Hello world')
    print(type(f))
a = open('output', 'w')
print(type(a))
import time
def log(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(end - start)
        return result
    return wrapper
a = log(zhao)
print(a([[2, 1, 1], [1, 1, 0], [0, 1, 1]] * 100))

a = [1, 3, 4, 5]
print(a[2:0:-1])