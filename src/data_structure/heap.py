class Heap(object):
    def __init__(self):
        self.array = []

    def percolateUpIteration(self, index):
        if index <= 0:
            return
        while index > 0:
            parentIndex = (index - 1) // 2
            if self.array[index] < self.array[parentIndex]:
                self.array[parentIndex], self.array[index] = self.array[index], self.array[parentIndex]
                index = parentIndex
            else:
                break

    def percolateUpRecursion(self, index):
        if index <= 0:
            return
        parentIndex = (index - 1) // 2
        if self.array[index] < self.array[parentIndex]:
            self.array[parentIndex], self.array[index] = self.array[index], self.array[parentIndex]
            self.percolateUpRecursion(self, parentIndex)

    def percolateDownIteration(self, index):
        if index > len(self.array) // 2 - 1:
            return
        while index <= len(self.array) // 2 - 1:
            indexLeftChild = index * 2 + 1
            indexRightChild = index * 2 + 2
            indexMinChild = indexLeftChild
            if indexRightChild < len(self.array) and self.array[indexRightChild] < self.array[indexLeftChild]:
                indexMinChild = indexRightChild
            if self.array[index] > self.array[indexMinChild]:
                self.array[index], self.array[indexMinChild] = self.array[indexMinChild], self.array[index]
                index = indexMinChild
            else:
                break

    def percolateDownRecursion(self, index):
        if index > len(self.array) // 2 - 1:
            return
        indexLeftChild = index * 2 + 1
        indexRightChild = index * 2 + 2
        indexMinChild = indexLeftChild
        if indexRightChild < len(self.array) and self.array[indexRightChild] < self.array[indexLeftChild]:
            indexMinChild = indexRightChild
        if self.array[index] > self.array[indexMinChild]:
            self.array[index], self.array[indexMinChild] = self.array[indexMinChild], self.array[index]
            self.percolateDownRecursion(self, indexMinChild)

    def isEmpty(self):
        return len(self.array) == 0

    def getSize(self):
        return len(self.array)

    def getTop(self):
        return self.array[0]

    def pop(self):
        if self.isEmpty():
            print('Heap is already empty!')
            return None
        result = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        if len(self.array) > 0:
            self.percolateDownIteration(0)
        return result

    def insert(self, number):
        self.array.append(number)
        self.percolateUpIteration(len(self.array) - 1)

testHeap = Heap()
testArray = [2, 4, 2 ,8, 5, 6, 1, 12, 9]
for element in testArray:
    testHeap.insert(element)
while not testHeap.isEmpty():
    print(testHeap.pop(), end=' ')
print()
# ----------------------------------------------------------------------------------
def findFirstKElement1(array, k):
    if array == None or len(array) <= k:
        return array
    heap = Heap()
    for element in array:
        heap.insert(element)
    result = []
    for i in range(k):
        result.append(heap.pop())
    return result

def findFirstKElement2(array, k):
    if array == None or len(array) <= k:
        return array
    heap = Heap()
    for i in range(len(array)):
        if i < k:
            heap.insert(-1 * array[i])
        else:
            if heap.getTop() < -1 * array[i]:
                heap.pop()
                heap.insert(-1 * array[i])
    result = []
    for i in range(k):
        result.append(-1 * heap.pop())
    return result

def findFirstKElement3(array, k, leftIndex, rightIndex):
    if array == None or rightIndex - leftIndex + 1 <= k or k <= 0:
        return
    leftBound = leftIndex
    rightBound = rightIndex - 1
    while leftBound <= rightBound:
        if array[leftBound] < array[rightIndex]:
            leftBound += 1
        else:
            array[leftBound], array[rightBound] = array[rightBound], array[leftBound]
            rightBound -= 1
    array[leftBound], array[rightIndex] = array[rightIndex], array[leftBound]
    numberOfSmaller = leftBound - leftIndex
    if k < numberOfSmaller:
        findFirstKElement3(array, k, leftIndex, leftBound - 1)
    elif k == numberOfSmaller:
        return # array[leftIndex:leftBound]
    elif k == numberOfSmaller + 1:
        return # array[leftIndex:leftBound + 1]
    else:
        findFirstKElement3(array, k - numberOfSmaller - 1, leftBound + 1, rightIndex)

print(findFirstKElement2(testArray, 3))
findFirstKElement3(testArray, 7, 0, len(testArray) - 1)
print(testArray[:7])
