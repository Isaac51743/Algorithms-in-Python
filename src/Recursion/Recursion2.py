def power2(a, b):
    if a == 0 and b <= 0:
        return None
    elif a != 0 and b < 0:
        return 1 / power1(a, -b)
    else:
        return power1(a, b)
# assuming b > 0 if a == 0, b >= 0 if a != 0
def power1(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    tem = power1(a, b//2)
    if b % 2 == 0:
        return tem * tem
    else:
        return tem * tem * a
print(power2(0, -1))

def mergesort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    leftpart = mergesort(array[:mid])
    rightpart = mergesort(array[mid:])
    result = merge(leftpart, rightpart)
    return result

# leftarray and rightarray will not be None at the same time
def merge(left, right):
    i = j = 0
    result = []
    while len(result) < len(left) + len(right):
        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i == len(left):
            result.extend(right[j:])
        elif j == len(right):
            result.extend(left[i:])
    return result

# row for current row, col record result
def nq(row, col, n):
    # print(col)
    if row >= n:
        for i, j in enumerate(col):
            print([i, j], end=' ')
        print()
        return
    for j in range(n):
        legal = True
        if j not in col:
            for idx in range(len(col)):
                # print([r, c])
                if row - idx == abs(j - col[idx]):
                    legal = False
                    break
            if legal:
                nq(row + 1, col + [j], n)

def spiralprint(array2D, offset, count):
    if offset == (len(array2D) - 1)//2 + 1:
        return array2D
    size = len(array2D) - 2 * offset
    if size == 1:
        array2D[offset][offset] = count
    else:
        for i in range(size - 1):
            r = offset
            c = offset + i
            array2D[r][c] = count
            count += 1
        for i in range(size - 1):
            r = offset + i
            c = offset + size - 1
            array2D[r][c] = count
            count += 1
        for i in range(size - 1):
            r = len(array2D) - 1 - offset
            c = len(array2D) - 1 - offset - i
            array2D[r][c] = count
            count += 1
        for i in range(size - 1):
            r = len(array2D) - 1 - offset - i
            c = offset
            array2D[r][c] = count
            count += 1
    return spiralprint(array2D, offset + 1, count)

def reversepair(head):
    if head == None or head.next == None:
        return head
    newhead = head.next
    head.next = reversepair(newhead.next)
    newhead.next = head
    return newhead
# not in-place, should reversestr(stlist, left, right)
def reversestr(st):
    if len(st) <= 1:
        return st
    result = st[-1] + reversestr(st[1:-1]) + st[0]
    return result

# no extra space
def reversestr1(stlist, left, right):
    if left >= right:
        return
    stlist[left], stlist[right] = stlist[right], stlist[left]
    reversestr1(stlist, left + 1, right - 1)

def isdigit(st):
    if ord(st) >= ord('0') and ord(st) <= ord('9'):
        return True
    return False
def abbrevmatch(st, abbre, start1, start2):
    if start1 == len(st) and start2 == len(abbre):
        return True
    elif start1 == len(st) or start2 == len(abbre):
        return False

    if isdigit(abbre[start2]):
        idx = start2             # idx for abbre
        num = 0
        # read the num
        while idx < len(abbre) and isdigit(abbre[idx]):
            num = num * 10 + ord(abbre[idx]) - ord('0')
            idx += 1
        if num > len(st) - start1:
            return False
        else:
            return abbrevmatch(st, abbre, start1 + num, idx)
    else:
        if st[start1] == abbre[start2]:
            return abbrevmatch(st, abbre, start1 + 1, start2 + 1)
        else:
            return False

def nodesnum(node):
    if node == None:
        return 0
    leftnum = nodesnum(node.left)
    rightnum = nodesnum(node.right)
    node.leftchilds = leftnum
    return leftnum + rightnum + 1

def differencemax(node):
    if node == None:
        return 0
    leftnum = differencemax(node.left)
    rightnum = differencemax(node.right)
    global maxdif
    global targetnode
    if abs(leftnum - rightnum) > maxdif:
        targetnode = node
        maxdif = abs(leftnum - rightnum)
    return leftnum + rightnum + 1

def LCA1(node, target1, target2):
    if node == None:
        return None
    elif node.value == target1 or node.value == target2:
        return node
    # step1 get value from child
    findinleft = LCA1(node.left, target1, target2)
    findinright = LCA1(node.right, target1, target2)
    # step2 + 3 operation in current layer and report
    if findinleft != None and findinright != None:
        return node
    elif findinleft != None:
        return findinleft
    elif findinright != None:
        return findinright
    else:
        return None

def LCA2(node, path, target):
    if node == None:
        return None
    if node.value == target:
        return path
    leftpath = LCA2(node.left, path + [node.left], target)
    rightpath = LCA2(node.right, path + [node.right], target)
    if leftpath != None:
        return leftpath
    elif rightpath != None:
        return rightpath
    else:
        return None

# ---------------------------------------------------------------------------
test = [1, 4, 2, 6, 2, 4, 1, 5, 0]
print(mergesort(test))
nq(0, [], 4)
# ---------------------------------------------------------------------------
n = 6
test1 = [[0] * n for _ in range(n)]
a = spiralprint(test1, 0, 1)
for r in range(len(a)):
    print(a[r])
# ---------------------------------------------------------------------------
class node():
    def __init__(self, n):
        self.next = None
        self.num = n
class linkedlist(object):
    def __init__(self):
        self.head = None

    def add(self, val):
        temnode = node(val)
        temnode.next = self.head
        self.head = temnode

    def show(self):
        cur = self.head
        while cur != None:
            print(cur.num, end=' ')
            cur = cur.next
        print()  # used to change the line
L = linkedlist()
for i in range(5):
    l=L.add(5 - i)
L.show()
L.head = reversepair(L.head)
L.show()
# ---------------------------------------------------------------------------
testst = 'abcdef'
stlist = list(testst)
print(reversestr(testst))
reversestr1(stlist, 0, len(stlist) - 1)
print(''.join(stlist))
# ---------------------------------------------------------------------------
st = 'zhaoyuehang'
abbre = 'z5e2ng'
print(abbrevmatch(st, abbre, 0, 0))
# ---------------------------------------------------------------------------
class treenode():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.leftchilds = 0
   #            0
   #          /    \
   #        1        2
   #      /        /   \
   #    3         4     5
   #  /   \
   # 6     7
nodelist = []
for i in range(8):
    nodelist.append(treenode(i))
nodelist[0].left = nodelist[1]
nodelist[0].right = nodelist[2]
nodelist[1].left = nodelist[3]
nodelist[2].left = nodelist[4]
nodelist[2].right = nodelist[5]
nodelist[3].left = nodelist[6]
nodelist[3].right = nodelist[7]
nodesnum(nodelist[0])
for node in nodelist:
    print(node.leftchilds, end=' ')
print()
# ---------------------------------------------------------------------------
maxdif = 0
targetnode = None
differencemax(nodelist[0])
print([targetnode.value, maxdif])
# ---------------------------------------------------------------------------
print(LCA1(nodelist[0], 3, 4).value)
# ---------------------------------------------------------------------------
path1 = LCA2(nodelist[0], [nodelist[0]], 2)
path2 = LCA2(nodelist[0], [nodelist[0]], 5)
i = 0
while i < len(path1) and i < len(path2):
    if path1[i].value != path2[i].value:
        break
    i += 1
result = path1[i - 1]
print(result.value)
