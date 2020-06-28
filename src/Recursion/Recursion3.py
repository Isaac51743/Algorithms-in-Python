class treenode():
    class_variable = 0
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.leftchilds = 0

   #            4
   #          /    \
   #        3        5
   #      /        /   \
   #    1         6     7
   #  /   \
   # 0     2
nodelist = []
for i in range(8):
    nodelist.append(treenode(i))
nodelist[4].left = nodelist[3]
nodelist[4].right = nodelist[5]
nodelist[3].left = nodelist[1]
nodelist[1].left = nodelist[0]
nodelist[1].right = nodelist[2]
nodelist[5].left = nodelist[6]
nodelist[5].right = nodelist[7]

def balancetree(node):
    if node == None:
        return 0
    leftheight = balancetree(node.left)
    rightheight = balancetree(node.right)
    if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
        return -1
    else:
        return max(leftheight, rightheight) + 1
print(balancetree(nodelist[0]) != -1)

def maxsumpath(node):
    if node == None:
        return 0
    leftcost = maxsumpath(node.left)
    rightcost = maxsumpath(node.right)
    temcost = leftcost + rightcost + node.value
    global result
    if node.left and node.right and temcost > result:
        result = temcost
    return max(leftcost, rightcost) + node.value
# -------------------------------------------------------------------------------------
def maxpathadv(node):
    if node == None:
        return 0
    leftcost = max(0, maxpathadv(node.left))
    rightcost = max(0, maxpathadv(node.right))
    temcost = leftcost + rightcost + node.value
    global result
    if temcost > result:
        result = temcost
    return max(leftcost, rightcost) + node.value

nodelist[6].value = -10
nodelist[0].value = -10
result = -10000
maxsumpath(nodelist[0])
print(result)
result = -10000
maxpathadv(nodelist[0])
print(result)
nodelist[6].value = 6
nodelist[0].value = 0
# -------------------------------------------------------------------------------------
finalsum = -100000
def maxpath(node, temsum):
    if node == None:
        return
    if node.left == None and node.right == None:
        global finalsum
        finalsum = max(temsum + node.value, finalsum)
    maxpath(node.left, temsum + node.value)
    maxpath(node.right, temsum + node.value)

maxpath(nodelist[0], 0)
print(finalsum)
# -------------------------------------------------------------------------------------
havetarget = False
def targetpath(node, record, target):
    if node == None:
        return

    record.append(0)
    for i in range(len(record)):
        record[i] += node.value
    print(record)
    global havetarget
    if target in record:
        havetarget = True
    targetpath(node.left, record, target)
    targetpath(node.right, record, target)
    del record[-1]
    for i in range(len(record)):
        record[i] -= node.value
def targetpathadv(node, record, pathprefix, target):
    if node == None:
        return
    # current layer
    global havetarget
    if pathprefix + node.value - target in record or pathprefix + node.value == target:
        havetarget = True
    # next layer
    if pathprefix + node.value in record:
        record[pathprefix + node.value] += 1
    else:
        record[pathprefix + node.value] = 1
    targetpathadv(node.left, record, pathprefix + node.value, target)
    targetpathadv(node.right, record, pathprefix + node.value, target)
    if record[pathprefix + node.value] == 1:
        del record[pathprefix + node.value]
    else:
        record[pathprefix + node.value] -= 1
def maxseg(node, record):
    if node ==None:
        return
    global maxsegment
    # if record[-1] + node.value > maxsegment:
    #     maxsegment = record[-1] + node.value
    if record[-1] + node.value - min(record) > maxsegment:
        maxsegment = record[-1] + node.value - min(record)
    record.append(record[-1] + node.value)
    maxseg(node.left, record)
    maxseg(node.right, record)
    del record[-1]
def maxsegadv(node, pathprefix):
    if node ==None:
        return
    global maxsegment
    if pathprefix < 0:
        newprefix = node.value
    else:
        newprefix = pathprefix + node.value
    if newprefix > maxsegment:
        maxsegment = newprefix
    maxsegadv(node.left, newprefix)
    maxsegadv(node.right, newprefix)


targetpath(nodelist[0], [], 12)
print(havetarget)
targetpathadv(nodelist[0], {}, 0, 12)
print(havetarget)
maxsegment = -100000
# nodelist[4].value = 19
# maxseg(nodelist[0], [0])
maxsegadv(nodelist[0], 0)
print(maxsegment)
# -------------------------------------------------------------------------------------
class listnode():
    def __init__(self, num):
        self.value = num
        self.pre = None
        self.next = None
head = end = None
def BSTtoLL(node):
    if node == None:
        return
    BSTtoLL(node.left)
    global head
    global end
    cur = listnode(node.value)
    if end == None:
        head = cur
    else:
        end.next = cur
        cur.pre = end
    end = cur
    BSTtoLL(node.right)
def printLL(node):
    if node == None:
        return
    print(node.value, end=' ')
    printLL(node.next)
BSTtoLL(nodelist[4])
printLL(head)
print()
# -------------------------------------------------------------------------------------
def deserialization(preorder, pre_l, pre_r, inorder, in_l, in_r, indexdic):
    if pre_l > pre_r:
        return None
    # current layer
    root = treenode(preorder[pre_l])
    leftsize = indexdic[preorder[pre_l]] - in_l
    root.left = deserialization(preorder, pre_l + 1, pre_l + leftsize, inorder, in_l, indexdic[preorder[pre_l]] - 1, indexdic)
    root.right = deserialization(preorder, pre_l + leftsize + 1, pre_r, inorder, indexdic[preorder[pre_l]] + 1, in_r, indexdic)
    return root
def levelin(level, inorder, in_l, in_r, indexdic):
    if in_l > in_r:
        return None
    root = treenode(level[0])
    leftsize = indexdic[level[0]] - in_l
    leftlevel = []
    rightlevel = []
    for item in level:
        if indexdic[item] < indexdic[level[0]]:
            leftlevel.append(item)
        else:
            rightlevel.append(item)
    root.left = levelin(leftlevel, inorder, in_l, in_l + leftsize - 1, indexdic)
    root.right = levelin(rightlevel, inorder, in_l + leftsize + 1, in_r, indexdic)
    return root
def preorder(node):
    if node == None:
        return None
    print(node.value, end=' ')
    preorder(node.left)
    preorder(node.right)
def inorder(node):
    if node == None:
        return None
    inorder(node.left)
    print(node.value, end=' ')
    inorder(node.right)
inseq = [3, 2, 1]
preseq = [1, 2, 3]
levelseq = [1, 2, 3]
indexdic = {}
for i in range(len(inseq)):
    indexdic[inseq[i]] = i

# root = deserialization(preseq, 0, len(preseq) - 1, inseq, 0, len(inseq) - 1, indexdic)
root = levelin(levelseq, inseq, 0, len(inseq) - 1, indexdic)
inorder(root)
print()
preorder(root)