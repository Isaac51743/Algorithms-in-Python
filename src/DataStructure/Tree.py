import DataStructure1 as DS1
print()
class TreeNode(object):
    def __init__(self, value = -1, leftChild = None, rightChild = None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
    def addLeft(self, node):
        self.leftChild = node
    def addRight(self, node):
        self.rightChild = node

testRoot1 = TreeNode(1)
testRoot1.addLeft(TreeNode(2))
testRoot1.addRight(TreeNode(3))
testRoot2 = TreeNode(1)
testRoot2.addLeft(TreeNode(3))
testRoot2.addRight(TreeNode(2))
testRoot3 = TreeNode(10)
testRoot3.addLeft(TreeNode(3))
testRoot3.addRight(TreeNode(12))
# testRoot1:
#                  1
#                /  \
#              2      3
# testRoot2:
#                    1
#                  /  \
#                3      2
# testRoot3:
#                   10
#                  /  \
#                3      12
def preOrder(root):
    if root == None:
        return
    print(root.value, end=' ')
    preOrder(root.leftChild)
    preOrder(root.rightChild)

def inOrder(root):
    if root == None:
        return
    inOrder(root.leftChild)
    print(root.value, end=' ')
    inOrder(root.rightChild)

def postOrder(root):
    if root == None:
        return
    postOrder(root.leftChild)
    postOrder(root.rightChild)
    print(root.value, end=' ')

preOrder(testRoot1)
print()
inOrder(testRoot1)
print()
postOrder(testRoot1)
print()
# -----------------------------------------------------------------------------------
def getHeight(root):
    if root == None:
        return 0
    leftHeight = getHeight(root.leftChild)
    rightheight = getHeight(root.rightChild)
    if leftHeight > rightheight:
        return leftHeight + 1
    else:
        return rightheight + 1

def isBalanced(root):
    if root == None:
        return True
    leftHeight = getHeight(root.leftChild)
    rightHeight = getHeight(root.rightChild)
    if abs(leftHeight - rightHeight) <= 1:
        return isBalanced(root.leftChild) and isBalanced(root.rightChild)
    else:
        return False

def isSymmetric(leftNode, rightNode):
    if leftNode == None and rightNode == None:
        return True
    elif leftNode == None or rightNode == None:
        return False
    elif leftNode.value == rightNode.value:
        return isSymmetric(leftNode.leftChild, rightNode.rightChild) and isSymmetric(leftNode.rightChild, rightNode.leftChild)
    else:
        return False

def isIdentical(leftRoot, rightRoot):
    if leftRoot == None and rightRoot == None:
        return True
    elif leftRoot == None or rightRoot == None:
        return False
    elif leftRoot.value == rightRoot.value:
        case1 = isIdentical(leftRoot.leftChild, rightRoot.leftChild) and isIdentical(leftRoot.rightChild, rightRoot.rightChild)
        case2 = isIdentical(leftRoot.rightChild, rightRoot.leftChild) and isIdentical(leftRoot.leftChild, rightRoot.rightChild)
        return case1 or case2
    else:
        return False

print('tree height: ' + str(getHeight(testRoot1)))
print(isBalanced(testRoot1))
print(isSymmetric(testRoot2.leftChild, testRoot2.rightChild))
print(isIdentical(testRoot1, testRoot2))
# -----------------------------------------------------------------------------------
def isBST(root, smallerBound, biggerBound):
    if root == None:
        return True
    if root.value > smallerBound and root.value < biggerBound:
        return isBST(root.leftChild, smallerBound, root.value) and isBST(root.rightChild, root.value, biggerBound)
    else:
        return False
def inOrderInRange(root, smallerBound, biggerBound):
    if root == None:
        return
    if root.value > smallerBound:
        inOrderInRange(root.leftChild, smallerBound, biggerBound)
    if root.value >= smallerBound and root.value <= biggerBound:
        print(root.value, end=' ')
    if root.value < biggerBound:
        inOrderInRange(root.rightChild, smallerBound, biggerBound)

print('whether a BST: ' + str(isBST(testRoot3, float('-inf'), float('inf'))))
inOrderInRange(testRoot3, 9, 20)
print()
# -----------------------------------------------------------------------------------
def searchBST(root, target):
    if root == None or root.value == target:
        return root
    if root.value > target:
        return searchBST(root.leftChild, target)
    else:
        return searchBST(root.rightChild, target)

def insertBSTRecursion1(root, target):
    if root == None:
        return TreeNode(target)
    if root.value > target:
        root.leftChild = insertBSTRecursion1(root.leftChild, target)
    elif root.value < target:
        root.rightChild = insertBSTRecursion1(root.rightChild, target)
    return root

def insertBSTIteration1(root, target):
    if root == None:
        return TreeNode(target)
    preNode = None
    curNode = root
    while curNode != None:
        preNode = curNode
        if curNode.value > target:
            curNode = curNode.leftChild
        elif curNode.value < target:
            curNode = curNode.rightChild
        else:
            return root
    if preNode.value > target:
        preNode.leftChild = TreeNode(target)
    elif preNode.value < target:
        preNode.rightChild = TreeNode(target)
    return root

def insertBSTRecursion2(root, target):
    if root == None:
        return TreeNode(target)
    helper(root, target)
    return root
def helper(root, target):
    if root.value > target:
        if root.leftChild != None:
            helper(root.leftChild, target)
        else:
            root.leftChild = TreeNode(target)
    elif root.value < target:
        if root.rightChild != None:
            helper(root.rightChild, target)
        else:
            root.rightChild = TreeNode(target)

def insertBSTIteration2(root, target):
    if root == None:
        return TreeNode(target)
    curNode = root
    while curNode.value != target:
        if curNode.value < target:
            if curNode.rightChild != None:
                curNode = curNode.rightChild
            else:
                curNode.rightChild = TreeNode(target)
                break
        elif curNode.value > target:
            if curNode.leftChild != None:
                curNode = curNode.leftChild
            else:
                curNode.leftChild = TreeNode(target)
                break
    return root
def removeBST(root, target):
    if root == None:
        return None
    if target < root.value:
        root.leftChild = removeBST(root.leftChild, target)
    elif target > root.value:
        root.rightChild = removeBST(root.rightChild, target)
    else:
        if root.leftChild == None:
            return root.rightChild
        elif root.rightChild == None:
            return root.leftChild
        else:
            if root.rightChild.leftChild == None:
                root.rightChild.leftChild = root.leftChild
                return root.right
            else:
                smallestOnRight = deleteMin(root.rightChild)
                smallestOnRight.leftChild = root.leftChild
                smallestOnRight.rightChild = root.rightChild
                return smallestOnRight
    return root
# assuming root must has left child
def deleteMin(root):
    preNode = root
    curNode = root.leftChild
    while curNode != None:
        preNode = curNode
        curNode = curNode.leftChild
    preNode.leftChild = curNode.rightChild
    return curNode

print(searchBST(testRoot3, 10))
newRoot3 = insertBSTRecursion2(testRoot3, 1)
print(searchBST(newRoot3, 1))
newRoot3 = insertBSTIteration2(newRoot3, 2)
print(searchBST(newRoot3, 2))
newRoot3 = removeBST(newRoot3, 1)
print(searchBST(newRoot3, 1))
#------------------------------------------------------------------------------------
def preOrderIteration(root):
    if root == None:
        return
    stack = DS1.Stack()
    stack.push(root)
    while not stack.isEmpty():
        curNode = stack.pop()
        print(curNode.value, end=' ')
        if curNode.rightChild != None:
            stack.push(curNode.rightChild)
        if curNode.leftChild != None:
            stack.push(curNode.leftChild)

def inOrderIteration(root):
    if root == None:
        return
    stack = DS1.Stack()
    nextNode = root
    while not stack.isEmpty() or nextNode != None:
        if nextNode != None:
            stack.push(nextNode)
            nextNode = nextNode.leftChild
        else: # top element is the stack has no left child any more
            curNode = stack.pop()
            print(curNode.value, end=' ')
            nextNode = curNode.rightChild
            
def postOrderIteration(root):
    if root == None:
        return
    preNode = None
    stack = DS1.Stack()
    stack.push(root)
    while not stack.isEmpty():
        curNode = stack.getTop()
        if preNode == None or preNode.leftChild == curNode or preNode.rightChild == curNode:
            if curNode.leftChild != None:
                stack.push(curNode.leftChild)
            elif curNode.rightChild != None:
                stack.push(curNode.rightChild)
            else:
                print(stack.pop().value, end=' ')
        elif curNode.leftChild == preNode:
            if curNode.rightChild != None:
                stack.push(curNode.rightChild)
            else:
                print(stack.pop().value, end=' ')
        else:
            print(stack.pop().value, end=' ')
        preNode = curNode

preOrderIteration(testRoot3)
print()
inOrderIteration(testRoot3)
print()
postOrderIteration(testRoot3)
print()

