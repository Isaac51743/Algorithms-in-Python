class node(object):
    def __init__(self, value = -1, lchild = None, rchild = None):
        self.val = value
        self.left = lchild
        self.right = rchild
    def addleft(self, node):
        self.left = node
    def addright(self, node):
        self.right = node

class tree(object):
    def __init__(self, node):
        self.root = node

class Queue(object):
    def __init__(self):
        self.array = []
    def push(self, item):
        self.array.append(item)
    def empty(self):
        return self.array == []
    def getsize(self):
        return len(self.array)
    def pop(self):
        if len(self.array) == 0:
            return None
        tem = self.array[0]
        self.array = self.array[1:]
        return tem

root1 = node(1)
root1.addleft(node(2))
root1.addright(node(3))
root2 = node(1)
root2.addleft(node(3))
root2.addright(node(2))
root3 = node(10)
root3.addleft(node(3))
root3.addright(node(12))
n1 = node(1)
n2 = node(2)
n3 = node(3)
n1.addleft(n2)
n1.addright(n3)
n2.addright(n3)

# root1:        1
#                /  \
#              2      3
# root2:         1
#                  /  \
#                3      2
# root3:         10
#                  /  \
#                3      12

def BFS(node):
    if node == None:
        return None
    queue = Queue()
    queue.push(node)
    while not queue.empty():
        size = queue.getsize()
        for i in range(size):
            tem = queue.pop()
            print(tem.val, end=' ')
            if tem.left != None:
                queue.push(tem.left)
            if tem.right != None:
                queue.push(tem.right)
        print()
def bipartite(node):
    if node == None:
        return None
    q = Queue()
    q.push(node)
    list1 = []
    list2 = []
    j = True
    while not q.empty():
        size = q.getsize()
        curlayer = []

        # for each layer
        for i in range(size):
            tem = q.pop()
            if j:
                list1.append(tem.val)
            else:
                list2.append(tem.val)
            if tem.left != None:
                q.push(tem.left)
                curlayer.append(tem.left.val)
            if tem.right != None:
                q.push(tem.right)
                curlayer.append(tem.right.val)

        for item in curlayer:
                if j and item in list1:
                    return False
                elif not j and item in list2:
                    return False
        j = not j
    return True
def complete(node):
    if node == None:
        return None
    q = Queue()
    q.push(node)
    key = True
    while not q.empty():
        tem = q.pop()
        if tem.left != None:
            if key:
                q.push(tem.left)
            else:
                return False
        else:
            key = False
        if tem.right != None:
            if key:
                q.push(tem.right)
            else:
                return False
        else:
            key = False
    return True

# BFS2
class heap(object):
    def __init__(self):
        self.array = []

    def percolateup(self,index):
        if index <= 0:
            return None
        parent = (index - 1) // 2
        if self.array[index][0] < self.array[parent][0]:
            tem = self.array[index]
            self.array[index] = self.array[parent]
            self.array[parent] = tem
            self.percolateup(parent)

    def percolatedown(self, index):
        left = index * 2 + 1
        right = left + 1
        if right <= len(self.array) - 1:
            if self.array[left][0] < self.array[right][0]:
                min = left
            else:
                min = right
            if self.array[index][0] > self.array[min][0]:
                tem = self.array[index]
                self.array[index] = self.array[min]
                self.array[min] = tem
                self.percolatedown(min)
        elif left <= len(self.array) - 1:
            if self.array[left][0] < self.array[index][0]:
                tem = self.array[left]
                self.array[left] = self.array[index]
                self.array[index] = tem
                self.percolatedown(left)

    def insert(self, val):
        self.array.append(val)
        self.percolateup(len(self.array) - 1)
        return self.array

    def update(self, index, val):
        if val[0] == self.array[index][0]:
            return self.array

        if val[0] > self.array[index][0]:
            self.array[index] = val
            self.percolatedown(index)
        elif val[0] < self.array[index][0]:
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

    def empty(self):
        return self.array == []

def kthsmal(matri, k):
    if matri == None:
        return None
    N = len(matri)
    pqueue = heap()
    pqueue.insert([matri[0][0], 0, 0])
    visit = {}
    for t in range(k):
        tem = pqueue.pop()
        row = tem[1]
        col = tem[2]
        if row + 1 <= N and (row + 1, col) not in visit:
            pqueue.insert([matri[row + 1][col], row + 1, col])
            visit[(row + 1, col)] = 1
        if col + 1 <= N and (row, col + 1) not in visit:
            pqueue.insert([matri[row][col + 1], row, col + 1])
            visit[(row, col + 1)] = 1
    return tem[0]

test = [[2, 6, 8, 10], [4, 7, 10, 12], [7, 10, 11, 14], [9, 11, 13, 15]]

BFS(root2)
print(bipartite(n1))
print(complete(root1))
r = kthsmal(test, 1)
print(r)