a = [1, 3, 6, 5, 4, 7]
class heap(object):
    def __init__(self):
        self.array = []

    def percolateup(self,index):
        if index <= 0:
            return None
        parent = (index - 1) // 2
        if self.array[index] < self.array[parent]:
            self.array[index], self.array[parent] = self.array[index], self.array[parent]
            self.percolateup(parent)

    def percolatedown(self, index):
        if index > len(self.array)//2 - 1:
            return
        left = index * 2 + 1
        right = left + 1
        min = left
        if right < len(self.array) and self.array[right] < self.array[left]:
            min = right
        if self.array[index] > self.array[min]:
            self.array[index], self.array[min] = self.array[index], self.array[min]
            self.percolatedown(min)


    def insert(self, val):
        self.array.append(val)
        self.percolateup(len(self.array) - 1)
        return self.array

    def update(self, index, val):
        if val == self.array[index]:
            return self.array

        if val > self.array[index]:
            self.array[index] = val
            self.percolatedown(index)
        elif val < self.array[index]:
            self.array[index] = val
            self.percolateup(index)
        return self.array

    def pop(self):
        if len(self.array) == 0:
            return None
        if len(self.array) == 1:
            tem = self.array[0]
            self.array = []
            return tem
        result = self.array[0]
        self.array[0] = self.array[-1]
        self.array = self.array[:-1]
        self.percolatedown(0)
        return result

d = heap()
d.array = a
e = d.pop()
print("original heap:" + str(d.array))
f = d.insert(1)
print("inserted heap:" + str(d.array))
g = d.update(0, 10)
print(d.array)

import heapq as hp
def firstk1(array, k):
    hp.heapify(array)
    for i in range(k):
        print(hp.heappop(array))
def firstk2(array, k):
    hh = heap()
    new = [item * -1 for item in array]
    for i in range(len(array)):
        if i < k:
            hh.insert(new[i])
        elif hh.array[0] < new[i]:
            hh.update(0, new[i])
        # print(hh.array)
    result = []

    for i in range(k):
        result.append(-1 * hh.pop())
    return result
def firstk3(array, k):
    if len(array) < k:
        return None
    if len(array) == k:
        return array

    # quicksort
    pivot = array[-1]
    i = 0
    j = len(array) - 2
    while i <= j:
        if array[i] < pivot:
            i += 1
        else:
            tem = array[i]
            array[i] = array[j]
            array[j] = tem
            j -= 1
    tem = array[-1]
    array[-1] = array[i]
    array[i] = tem

    if k < i:
        result = firstk3(array[:i], k)
        return result
    elif k == i or k == i + 1:
        return array[:k]
    else:
        sorted = array[:i + 1]
        # print(sorted)
        remain = firstk3(array[i + 1:], k - i - 1)
        return sorted + remain

b = [4, 6, 2, 7, 0, 34, 3]
c = [1, 2]
print(firstk2(b, 5))
