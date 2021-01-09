import tree as t
import data_structure1 as ds1
# import heap as h


def bfs1(root):
    if not root:
        return
    queue = ds1.Queue()
    queue.push(root)
    while not queue.is_empty():
        level_size = queue.get_size()
        for i in range(level_size):
            temp = queue.pop()
            if temp.left_child:
                queue.push(temp.left_child)
            if temp.right_child:
                queue.push(temp.right_child)
            print(temp.value, end=' ')
        print()


bfs1(t.test_root3)


def is_bipartite(root):
    if not root:
        return True
    queue = ds1.Queue()
    pre = {root}
    cur = set()
    visited = set()
    queue.push(root)
    while not queue.is_empty():
        level_size = queue.get_size()
        for i in range(level_size):
            temp = queue.pop()
            visited.add(temp)
            if temp.left_child and temp.left_child not in visited:
                if temp.left_child in pre:
                    return False
                cur.add(temp.left_child)
                queue.push(temp.left_child)

            if temp.right_child and temp.right_child not in visited:
                if temp.right_child in pre:
                    return False
                cur.add(temp.left_child)
                queue.push(temp.right_child)
        cur, pre = pre, cur
    return True


print(is_bipartite(t.test_root3))


def is_complete_tree(root):
    if not root:
        return True
    queue = ds1.Queue()
    queue.push(root)
    last_parent_passed = False
    while not queue.is_empty():
        temp = queue.pop()
        if not temp.left_child or temp.right_child:
            return False
        if last_parent_passed and (temp.left_child or temp.right_child):
            return False

        if temp.left_child:
            queue.push(temp.left_child)
        else:
            last_parent_passed = True

        if temp.right_child:
            queue.push(temp.right_child)
        else:
            last_parent_passed = True
    return True


print(is_complete_tree(t.test_root3))
# t.removeBST(t.test_root3, 12)
# print(is_complete_tree(t.test_root3))
# t.insertBSTIteration1(t.test_root3, 12)

# class HeapAdv(H.Heap):
#     def __init__(self):
#         H.Heap.__init__(self)
#     # @Override
#     def percolateUpIteration(self, index):
#         if index <= 0:
#             return
#         while index > 0:
#             parentIndex = (index - 1) // 2
#             if self.array[index][0] < self.array[parentIndex][0]:
#                 self.array[parentIndex], self.array[index] = self.array[index], self.array[parentIndex]
#                 index = parentIndex
#             else:
#                 break
#
#     def percolateDownIteration(self, index):
#         if index > len(self.array) // 2 - 1:
#             return
#         while index <= len(self.array) // 2 - 1:
#             indexLeftChild = index * 2 + 1
#             indexRightChild = index * 2 + 2
#             indexMinChild = indexLeftChild
#             if indexRightChild < len(self.array) and self.array[indexRightChild][0] < self.array[indexLeftChild][0]:
#                 indexMinChild = indexRightChild
#             if self.array[index][0] > self.array[indexMinChild][0]:
#                 self.array[index], self.array[indexMinChild] = self.array[indexMinChild], self.array[index]
#                 index = indexMinChild
#             else:
#                 break
#
# def findKSmallestOfSortedMatrix(matrix, k):
#     if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0 or k == 0:
#         return None
#     if k > len(matrix) * len(matrix[0]):
#         result = []
#         for row in range(len(matrix)):
#             for column in range(len(matrix[0])):
#                 result.append(matrix[row][column])
#         return result
#     visited = set()
#     heap = HeapAdv()
#     heap.insert([matrix[0][0], 0, 0])
#     visited.add((0, 0))
#     result = []
#     for i in range(k):
#         curNode = heap.pop()
#         result.append(curNode[0])
#         row1 = curNode[1]
#         column1 = curNode[2] + 1
#         row2 = curNode[1] + 1
#         column2 = curNode[2]
#         if column1 < len(matrix[0]) and (row1, column1) not in visited:
#             heap.insert([matrix[row1][column1], row1, column1])
#             visited.add((row1,column1))
#         if row2 < len(matrix) and (row2, column2) not in visited:
#             heap.insert([matrix[row2][column2], row2, column2])
#             visited.add((row2, column2))
#     return result
#
# testMatrix = [[2, 6, 8, 10], [4, 7, 10, 12], [7, 10, 11, 14], [9, 11, 13, 15]]
# print(findKSmallestOfSortedMatrix(testMatrix, 4))
