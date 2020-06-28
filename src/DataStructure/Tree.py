class Stack(object):
    def __init__(self):
        self.array = []
        self.top = None
    def push(self, item):
        self.array.append(item)
        self.top = len(self.array) - 1
    def empty(self):
        return self.array == []
    def gettop(self):
        if len(self.array) == 0:
            return None
        else:
            return self.array[self.top]
    def pop(self):
        if len(self.array) == 0:
            return None
        elif len(self.array) == 1:
            tem = self.array[self.top]
            self.top = None
            self.array = self.array[:-1]
            return tem
        else:
            tem = self.array[self.top]
            self.top = len(self.array) - 2
            self.array = self.array[:-1]
            return tem
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

root1 = node(1)
root1.addleft(node(2))
root1.addright(node(3))
root2 = node(1)
root2.addleft(node(3))
root2.addright(node(2))
root3 = node(10)
root3.addleft(node(3))
root3.addright(node(12))
# root1:        1
#                /  \
#              2      3
# root2:         1
#                  /  \
#                3      2
# root3:         10
#                  /  \
#                3      12
def inorder(node):
    if node == None:
        return node
    inorder(node.left)
    print(node.val, end=' ')
    inorder(node.right)
def search(root, target):
    if root == None or root.val == target:
        return root
    if target > root.val:
        return search(root.right, target)
    else:
        return search(root.left, target)
def insert(root, target):
    if root == None:
        return node(target)
    if root.val > target:
        root.left = insert(root.left, target)
    elif root.val < target:
        root.right = insert(root.right, target)
    return root
def insertIterative(root, target):
    if root == None:
        return node(target)
    pre = None
    cur = root
    while cur != None:
        pre = cur
        if cur.val > target:
            cur = cur.left
        elif cur.val < target:
            cur = cur.right
        else:
            return root
    if pre.val > target:
        pre.left = node(target)
    else:
        pre.right = node(target)
    return root
def insert1(root, target):
    if root == None:
        return node(target)
    helper(root, target)
def helper(root, target):
    if root.val == target:
        return
    if root.val > target:
        if root.left == None:
            root.left = node(target)
        else:
            helper(root.left, target)
    elif root.val < target:
        if root.right == None:
            root.right = node(target)
        else:
            helper(root.right, target)
def insert2(root, target):
    if root == None:
        return node(target)
    cur = root
    while cur.val != target:
        if cur.val > target:
            if cur.left != None:
                cur = cur.left
            else:
                cur.left = node(target)
                break
        elif cur.val < target:
            if cur.right != None:
                cur = cur.right
            else:
                cur.right = node(target)
                break
    return root
def remove(root, target):
    if root == None:
        return None
    if target > root.val:
        root.right = remove(root.right, target)
    elif target < root.val:
        root.left = remove(root.left, target)
    else: # root.val == target
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            if root.right.left == None:
                root.right.left = root.left
                return root.right
            else:
                smallest = deletemin(root.right)
                smallest.left = root.left
                smallest.right = root.right
            return smallest
    return root
def deletemin(root):
    while root.left != None:
        pre = root
        root = root.left
    pre.left = root.right
    return root
def getheight(node):
    if node == None:
        return 0
    leftheight = getheight(node.left)
    rightheight = getheight(node.right)
    if leftheight > rightheight:
        return leftheight + 1
    else:
        return rightheight + 1
# def getheight(node):
#     if node == None:
#         return 0
#     leftheight = getheight(node.left)
#     rightheight = getheight(node.right)
#     if leftheight > rightheight:
#         return leftheight + 1
#     else:
#         return rightheight + 1
def balanced(node):
    if node == None:
        return True
    leftheight = getheight(node.left)
    rightheight = getheight(node.right)
    if abs(leftheight - rightheight) <= 1:
        return balanced(node.left) and balanced(node.right)
    else:
        return False
# def balanced(node):
#     if node == None:
#         return True
#     leftheight = getheight(node.left)
#     rightheight = getheight(node.right)
#     if abs(leftheight - rightheight) <= 1:
#         return balanced(node.left) and balanced(node.right)
#     else:
#         return False

# def symmetric(left, right):
#     if left == None and right == None:
#         return True
#     elif (left == None and right != None) or (right == None and left != None):
#         return False
#     elif left.val != right.val:
#         return False
#     return symmetric(left.left, right.right) and symmetric(left.right, right.left)
def symmetric(left, right):
    if left == None and right == None:
        return True
    elif left == None or right == None:
        return False
    elif left.val != right.val:
        return False
    else:
        return symmetric(left.left, right.right) and symmetric(left.right, right.left)
# def identical(left, right):
#     if left == None and right == None:
#         return True
#     elif left == None or right == None:
#         return False
#     elif left.val != right.val:
#         return False
#     return (identical(left.left, right.right) and identical(left.right, right.left)) or (identical(left.left, right.left) and identical(left.right, right.right))
def identical(left, right):
    if left == None and right == None:
        return True
    elif left != None or right != None:
        return False
    elif left.val != right.val:
        return False
    else:
        case1 = identical(left.left, right.right) and identical(left.right, right.left)
        case2 = identical(left.left, right.left) and identical(left.right, right.right)
        return case1 or case2
import math
def BST(node, small, big):
    if node == None:
        return True
    if node.val > small and node.val < big:
        return BST(node.left, small, node.val) and BST(node.right, node.val, big)
    else:
        return False
def inorderrange(node, small, big):
    if node == None:
        return node

    inorderrange(node.left, small, big)
    if node.val >= small and node.val <= big:
        print(node.val, end=' ')
    inorderrange(node.right, small, big)
def inorderrangeA(node, small, big):
    if node == None:
        return None

    if node.val > small:
        inorderrangeA(node.left, small, big)
    if node.val > small and node.val < big:
        print(node.val, end=' ')
    if node.val < big:
        inorderrangeA(node.right, small, big)
inorder(root2)
print()
print(getheight(root2))
print(symmetric(root1, root2))
print(identical(root1, root1))
print(BST(root3, -math.inf, math.inf))
inorderrangeA(root3, 0, 11)
print()
insert2(root1, 38)
print(search(root1, 38).val)
remove(root1, 38)
print(search(root1, 38))

def preorderiter(root):
    if root == None:
        return None
    result = []
    s = Stack()
    s.push(root)
    while not s.empty():
        cur = s.pop()
        result.append(cur.val)
        if cur.right != None:
            s.push(cur.right)
        if cur.left != None:
            s.push(cur.left)
    return result
def inorderiter(root):
    if root == None:
        return None
    result = []
    s = Stack()
    next = root
    while not s.empty() or next != None:
        if next != None:
            s.push(next)
            next = next.left
        else:
            cur = s.pop()
            result.append(cur.val)
            next = cur.right
    return result
def postorder(root):
    if root == None:
        return None
    result = []
    s = Stack()
    s.push(root)
    pre = None
    while not s.empty():
        cur = s.gettop()
        if pre == None or pre.left == cur or pre.right == cur:
            if cur.left != None:
                s.push(cur.left)
            elif cur.right != None:
                s.push(cur.right)
            else:
                result.append(s.pop().val)
        elif pre == cur.left:
            if cur.right != None:
                s.push(cur.right)
            else:
                result.append(s.pop().val)
        else:
            result.append(s.pop().val)
        pre = cur
    return result
print(preorderiter(root1))
print(inorderiter(root1))
print(postorder(root1))


