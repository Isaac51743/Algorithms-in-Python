import Tree as T
import DataStructure1 as DS1
import Heap as H
print()
def BFS1(root):
    if root == None:
        return
    queue = DS1.Queue()
    queue.push(root)
    while not queue.isEmpty():
        numberOfNodeThisLayer = queue.getSize()
        for i in range(numberOfNodeThisLayer):
            curNode = queue.pop()
            print(curNode.value, end=' ')
            if curNode.leftChild != None:
                queue.push(curNode.leftChild)
            if curNode.rightChild != None:
                queue.push(curNode.rightChild)
        print()

BFS1(T.testRoot3)

def isBipartite(root):
    if root == None:
        return False
    group1 = set()
    group2 = set()
    isGroup1 = True
    queue = DS1.Queue()
    queue.push(root)
    while not queue.isEmpty():
        numberOfNodeThisLayer = queue.getSize()
        for i in range(numberOfNodeThisLayer):
            curNode = queue.pop()
            if isGroup1:
                if curNode in group2:
                    return False
                else:
                    group1.add(curNode)
            else:
                if curNode in group1:
                    return False
                else:
                    group2.add(curNode)

            if curNode.leftChild != None:
                queue.push(curNode.leftChild)
            if curNode.rightChild != None:
                queue.push(curNode.rightChild)
        isGroup1 = not isGroup1
    return True

print(isBipartite(T.testRoot3))

def isCompleteTree(root):
    if root == None:
        return True
    queue = DS1.Queue()
    queue.push(root)
    lastParentTraversed = False
    while not queue.isEmpty():
        curNode = queue.pop()
        if lastParentTraversed and (curNode.leftChild != None or curNode.rightChild != None):
                return False
        if curNode.leftChild != None:
            queue.push(curNode.leftChild)
        else:
            lastParentTraversed = True
        if curNode.rightChild != None:
            queue.push(curNode.rightChild)
        else:
            lastParentTraversed = True
    return True

print(isCompleteTree(T.testRoot3))
T.removeBST(T.testRoot3, 12)
print(isCompleteTree(T.testRoot3))
T.insertBSTIteration1(T.testRoot3, 12)
# ----------------------------------------------------------------------------------
class HeapAdv(H.Heap):
    def __init__(self):
        H.Heap.__init__(self)
    # @Override
    def percolateUpIteration(self, index):
        if index <= 0:
            return
        while index > 0:
            parentIndex = (index - 1) // 2
            if self.array[index][0] < self.array[parentIndex][0]:
                self.array[parentIndex], self.array[index] = self.array[index], self.array[parentIndex]
                index = parentIndex
            else:
                break

    def percolateDownIteration(self, index):
        if index > len(self.array) // 2 - 1:
            return
        while index <= len(self.array) // 2 - 1:
            indexLeftChild = index * 2 + 1
            indexRightChild = index * 2 + 2
            indexMinChild = indexLeftChild
            if indexRightChild < len(self.array) and self.array[indexRightChild][0] < self.array[indexLeftChild][0]:
                indexMinChild = indexRightChild
            if self.array[index][0] > self.array[indexMinChild][0]:
                self.array[index], self.array[indexMinChild] = self.array[indexMinChild], self.array[index]
                index = indexMinChild
            else:
                break

def findKSmallestOfSortedMatrix(matrix, k):
    if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0 or k == 0:
        return None
    if k > len(matrix) * len(matrix[0]):
        result = []
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                result.append(matrix[row][column])
        return result
    visited = set()
    heap = HeapAdv()
    heap.insert([matrix[0][0], 0, 0])
    visited.add((0, 0))
    result = []
    for i in range(k):
        curNode = heap.pop()
        result.append(curNode[0])
        row1 = curNode[1]
        column1 = curNode[2] + 1
        row2 = curNode[1] + 1
        column2 = curNode[2]
        if column1 < len(matrix[0]) and (row1, column1) not in visited:
            heap.insert([matrix[row1][column1], row1, column1])
            visited.add((row1,column1))
        if row2 < len(matrix) and (row2, column2) not in visited:
            heap.insert([matrix[row2][column2], row2, column2])
            visited.add((row2, column2))
    return result

testMatrix = [[2, 6, 8, 10], [4, 7, 10, 12], [7, 10, 11, 14], [9, 11, 13, 15]]
print(findKSmallestOfSortedMatrix(testMatrix, 4))
