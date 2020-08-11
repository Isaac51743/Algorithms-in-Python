import tree as T
import data_structure2 as DS2
print()
print('Recursion3:')
#            4
#          /    \
#        3        5
#      /        /   \
#    1         6     7
#  /   \
# 0     2
treeNodeList = []
for i in range(8):
    treeNodeList.append(T.TreeNode(i))
treeNodeList[4].leftChild = treeNodeList[3]
treeNodeList[4].rightChild = treeNodeList[5]
treeNodeList[3].leftChild = treeNodeList[1]
treeNodeList[1].leftChild = treeNodeList[0]
treeNodeList[1].rightChild = treeNodeList[2]
treeNodeList[5].leftChild = treeNodeList[6]
treeNodeList[5].rightChild = treeNodeList[7]

def isBalancedTree(root):
    if root == None:
        return 0
    leftHeight = isBalancedTree(root.leftChild)
    rightHeight = isBalancedTree(root.rightChild)
    if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
        return -1
    else:
        return max(leftHeight, rightHeight) + 1

print('is balanced tree:', isBalancedTree(treeNodeList[0]) != -1)
# -----------------------------------------------------------------------------------
def findMaxSumFromLeafToLeaf(root):
    if root == None:
        return 0
    leftSumOfPath = findMaxSumFromLeafToLeaf(root.leftChild)
    rightSumOfPath = findMaxSumFromLeafToLeaf(root.rightChild)
    global maxSumFromLeafToLeaf
    if root.leftChild and root.rightChild and maxSumFromLeafToLeaf < leftSumOfPath + rightSumOfPath + root.value:
        maxSumFromLeafToLeaf = leftSumOfPath + rightSumOfPath + root.value
    return max(leftSumOfPath, rightSumOfPath) + root.value

def findMaxSumOfAnyPath(root):
    if root == None:
        return 0
    leftSumOfPath = max(0, findMaxSumFromLeafToLeaf(root.leftChild))
    rightSumOfPath = max(0, findMaxSumFromLeafToLeaf(root.rightChild))
    global maxSumFromLeafToLeaf
    if maxSumFromLeafToLeaf < leftSumOfPath + rightSumOfPath + root.value:
        maxSumFromLeafToLeaf = leftSumOfPath + rightSumOfPath + root.value
    return max(leftSumOfPath, rightSumOfPath) + root.value

treeNodeList[6].value = -10
treeNodeList[0].value = -10
maxSumFromLeafToLeaf = float('-inf')
findMaxSumFromLeafToLeaf(treeNodeList[4])
print('sum of max path from leaf to leaf', maxSumFromLeafToLeaf)

maxSumOfPath = float('-inf')
findMaxSumOfAnyPath(treeNodeList[5])
print('sum of max path in the tree', maxSumOfPath)
treeNodeList[6].value = 6
treeNodeList[0].value = 0
# -----------------------------------------------------------------------------------
# down to up
def findMaxSumFromRootToLeaf(root):
    if root == None:
        return 0
    leftSumOfPath = findMaxSumFromRootToLeaf(root.leftChild)
    rightSumOfPath = findMaxSumFromRootToLeaf(root.rightChild)
    return max(leftSumOfPath, rightSumOfPath) + root.value
# up to down
def findMaxSumFromRootToLeafUpToDown(root, temporarySum):
    if root == None:
        return
    if root.leftChild == None and root.rightChild == None:
        global maxSumFromRootToLeaf
        maxSumFromRootToLeaf = max(maxSumFromRootToLeaf, temporarySum + root.value)
    findMaxSumFromRootToLeafUpToDown(root.leftChild, temporarySum + root.value)
    findMaxSumFromRootToLeafUpToDown(root.rightChild, temporarySum + root.value)

print('maxSumFromRootToLeaf(down to up):', findMaxSumFromRootToLeaf(treeNodeList[4]))
maxSumFromRootToLeaf = float('-inf')
findMaxSumFromRootToLeafUpToDown(treeNodeList[4], 0)
print('maxSumFromRootToLeaf(up to down):', maxSumFromRootToLeaf)
# -----------------------------------------------------------------------------------
def findSinglePathWithTargetSum(root, sumEndWithPreviousNode, targetSum):
    if root == None:
        return
    global pathExisted
    sumEndWithPreviousNode.append(0)
    for index in range(len(sumEndWithPreviousNode)):
        sumEndWithPreviousNode[index] += root.value
    if targetSum in sumEndWithPreviousNode:
        pathExisted = True
    findSinglePathWithTargetSum(root.leftChild, sumEndWithPreviousNode, targetSum)
    findSinglePathWithTargetSum(root.rightChild, sumEndWithPreviousNode, targetSum)
    sumEndWithPreviousNode.pop()
    for index in range(len(sumEndWithPreviousNode)):
        sumEndWithPreviousNode[index] -= root.value

def findSinglePathWithTargetSumAdv(root, pathPrefixRecord, pathPrefix, targetSum):
    if root == None:
        return
    global pathExisted
    if pathPrefix + root.value == targetSum or pathPrefix + root.value - targetSum in pathPrefixRecord:
        pathExisted = True
    if pathPrefix + root.value in pathPrefixRecord:
        pathPrefixRecord[pathPrefix + root.value] += 1
    else:
        pathPrefixRecord[pathPrefix + root.value] = 1
    findSinglePathWithTargetSumAdv(root.leftChild, pathPrefixRecord, pathPrefix + root.value, targetSum)
    findSinglePathWithTargetSumAdv(root.rightChild, pathPrefixRecord, pathPrefix + root.value, targetSum)
    if pathPrefixRecord[pathPrefix + root.value] > 1:
        pathPrefixRecord[pathPrefix + root.value] -= 1
    else:
        del pathPrefixRecord[pathPrefix + root.value]

pathExisted = False
findSinglePathWithTargetSum(treeNodeList[4], [], 12)
print('path Existed?', pathExisted)
findSinglePathWithTargetSumAdv(treeNodeList[0], {}, 0, 12)
print('path Existed?', pathExisted)
# -----------------------------------------------------------------------------------
def findMaxSumOfSinglePath1(root, pathPrefix):
    if root == None:
        return
    global maxSumOfSinglePath
    if pathPrefix > 0:
        maxSumOfSinglePath = max(maxSumOfSinglePath, pathPrefix + root.value)
    else:
        maxSumOfSinglePath = max(maxSumOfSinglePath, root.value)
    findMaxSumOfSinglePath1(root.leftChild, pathPrefix + root.value)
    findMaxSumOfSinglePath1(root.rightChild, pathPrefix + root.value)

def findMaxSumOfSinglePath2(root):
    if root == None:
        return 0
    global maxSumOfSinglePath
    leftMaxSum = findMaxSumOfSinglePath2(root.leftChild)
    rightMaxSum = findMaxSumOfSinglePath2(root.rightChild)
    if leftMaxSum < 0 and rightMaxSum < 0:
        currentMaxSum = root.value
    else:
        currentMaxSum = max(leftMaxSum, rightMaxSum) + root.value
    maxSumOfSinglePath = max(maxSumOfSinglePath, currentMaxSum)
    return currentMaxSum

maxSumOfSinglePath = float('-inf')
findMaxSumOfSinglePath1(treeNodeList[4], 0)
print('maxSumOfSinglePath:', maxSumOfSinglePath)

treeNodeList[4].value = -19
maxSumOfSinglePath = float('-inf')
findMaxSumOfSinglePath2(treeNodeList[4])
print('maxSumOfSinglePath:', maxSumOfSinglePath)
treeNodeList[4].value = 4
# -------------------------------------------------------------------------------------
def treeToLinkedList(root):
    if root == None:
        return None
    head = tail = None

    def inorderTraverse(root):
        if root == None:
            return
        nonlocal head, tail
        inorderTraverse(root.leftChild)
        if tail == None:
            head = DS2.ListNode(root.value)
            tail = head
        else:
            tail.next = DS2.ListNode(root.value)
            tail = tail.next
        inorderTraverse(root.rightChild)

    inorderTraverse(root)
    return head

DS2.linkedListPrint(treeToLinkedList(treeNodeList[4]))
# -------------------------------------------------------------------------------------
def preorderToTree(preorderArray, leftIndexPreorder, rightIndexPreorder, inorderArray, leftIndexInorder, rightIndexInorder, inorderDictionary):
    if leftIndexPreorder > rightIndexPreorder:
        return None
    root = T.TreeNode(preorderArray[leftIndexPreorder])
    leftSize = inorderDictionary[preorderArray[leftIndexPreorder]] - leftIndexInorder
    root.leftChild = preorderToTree(preorderArray, leftIndexPreorder + 1, leftIndexPreorder + leftSize, inorderArray, leftIndexInorder, inorderDictionary[preorderArray[leftIndexPreorder]] - 1, inorderDictionary)
    root.rightChild = preorderToTree(preorderArray, leftIndexPreorder + leftSize + 1, rightIndexPreorder, inorderArray, inorderDictionary[preorderArray[leftIndexPreorder]] + 1, rightIndexInorder, inorderDictionary)
    return root

def levelorderToTree(levelorderArray, inorderArray, leftIndexInorder, rightIndexInorder, inorderDictionary):
    if leftIndexInorder > rightIndexInorder:
        return None
    root = T.TreeNode(levelorderArray[0])
    leftSize = inorderDictionary[levelorderArray[0]] - leftIndexInorder
    leftLevelorder = []
    rightLevelorder = []
    for index in range(1, len(levelorderArray)):
        if inorderDictionary[levelorderArray[index]] < inorderDictionary[levelorderArray[0]]:
            leftLevelorder.append(levelorderArray[index])
        else:
            rightLevelorder.append(levelorderArray[index])
    root.leftChild = levelorderToTree(leftLevelorder, inorderArray, 0, inorderDictionary[levelorderArray[0]] - 1, inorderDictionary)
    root.rightChild = levelorderToTree(rightLevelorder, inorderArray, inorderDictionary[levelorderArray[0]] + 1, rightIndexInorder, inorderDictionary)
    return root

inorderArray = [3, 2, 1]
preorderArray = [1, 2, 3]
inorderDictionaryOfIndex = {}
for index in range(len(inorderArray)):
    inorderDictionaryOfIndex[inorderArray[index]] = index

testRoot1 = preorderToTree(preorderArray, 0, len(preorderArray) - 1, inorderArray, 0, len(inorderArray) - 1, inorderDictionaryOfIndex)
T.inOrder(testRoot1)
print()
T.preOrder(testRoot1)
print()

levelorderArray = [1, 2, 3]
testRoot2 = levelorderToTree(levelorderArray, inorderArray, 0, len(inorderArray) - 1, inorderDictionaryOfIndex)
T.inOrder(testRoot2)
print()
T.preOrder(testRoot2)
print()

