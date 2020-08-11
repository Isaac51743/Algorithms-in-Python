import data_structure2 as DS2
import tree as T
print('Recursion2:')
# -----------------------------------------------------------------------------------
def reverseEachPairInLinkedList(head):
    if head == None or head.next == None:
        return head
    newHead = head.next
    head.next = reverseEachPairInLinkedList(head.next.next)
    newHead.next = head
    return newHead

testHead = DS2.ListNode(6)
curNode = testHead
for i in range(5):
    curNode.next = DS2.ListNode(5 - i)
    curNode = curNode.next
DS2.linkedListPrint(testHead)
DS2.linkedListPrint(reverseEachPairInLinkedList(testHead))
# -----------------------------------------------------------------------------------
def isDigit(letter):
    if ord(letter) >= ord('0') and ord(letter) <= ord('9'):
        return True
    return False
def abbrevMatch(text, abbrev, indexOfText, indexOfAbbrev):
    if indexOfText == len(text) and indexOfAbbrev == len(abbrev):
        return True
    elif indexOfText == len(text) or indexOfAbbrev == len(abbrev):
        return False
    if isDigit(abbrev[indexOfAbbrev]):
        number = 0
        while isDigit(abbrev[indexOfAbbrev]):
            number = number * 10 + ord(abbrev[indexOfAbbrev]) - ord('0')
            indexOfAbbrev += 1
        if indexOfText + number - 1 < len(text):
            return abbrevMatch(text, abbrev, indexOfText + number, indexOfAbbrev)
        else:
            return False
    else:
        if abbrev[indexOfAbbrev] == text[indexOfText]:
            return abbrevMatch(text, abbrev, indexOfText + 1, indexOfAbbrev + 1)
        else:
            return False

testText = 'this code is soooooo perfect like an art.'
abbrev = 't11 s6 perfect l10.'
print(abbrevMatch(testText, abbrev, 0, 0))
# -----------------------------------------------------------------------------------
# edge length must > 3
def setNQueenInAChess(curRow, columnsInVisitedRows, edgeLength):
    if curRow == edgeLength:
        for row, column in enumerate(columnsInVisitedRows):
            print((row, column), end=' ')
        print()
        return
    for column in range(edgeLength):
        positionLegal = True
        for row in range(len(columnsInVisitedRows)):
            if column == columnsInVisitedRows[row] or curRow - row == abs(columnsInVisitedRows[row] - column):
                positionLegal = False
                break
        if positionLegal:
            columnsInVisitedRows.append(column)
            setNQueenInAChess(curRow + 1, columnsInVisitedRows, edgeLength)
            columnsInVisitedRows.pop()

setNQueenInAChess(0, [], 5)
# -----------------------------------------------------------------------------------
def spiralFillASquareMatrix(matrix, numOfVisitedLayers, count):
    if len(matrix) == 0:
        return None
    if numOfVisitedLayers >= (len(matrix) + 1) // 2:
        return matrix
    edgeLength = len(matrix) - 2 * numOfVisitedLayers
    print(edgeLength, numOfVisitedLayers)
    if edgeLength == 1:
        matrix[numOfVisitedLayers][numOfVisitedLayers] = count
        count += 1
    else:
        for shift in range(edgeLength - 1):
            matrix[numOfVisitedLayers][numOfVisitedLayers + shift] = count
            count += 1
        for shift in range(edgeLength - 1):
            matrix[numOfVisitedLayers + shift][numOfVisitedLayers + edgeLength - 1] = count
            count += 1
        for shift in range(edgeLength - 1):
            matrix[numOfVisitedLayers + edgeLength - 1][numOfVisitedLayers + edgeLength - 1 - shift] = count
            count += 1
        for shift in range(edgeLength - 1):
            matrix[numOfVisitedLayers + edgeLength - 1 - shift][numOfVisitedLayers] = count
            count += 1
    return spiralFillASquareMatrix(matrix, numOfVisitedLayers + 1, count)

edgeLength = 5
testMatrix = [[0 for _ in range(edgeLength)] for _ in range(edgeLength)]
filledMatrix = spiralFillASquareMatrix(testMatrix, 0, 0)
for row in range(len(filledMatrix)):
    print(filledMatrix[row])
# -----------------------------------------------------------------------------------
def countNumberOfNodesInLeftSubtree(root):
    if root == None:
        return 0
    numOfNodesOnLeft = countNumberOfNodesInLeftSubtree(root.leftChild)
    numOfNodesOnRight = countNumberOfNodesInLeftSubtree(root.rightChild)
    root.numberLeftChilds = numOfNodesOnLeft
    return numOfNodesOnLeft + numOfNodesOnRight + 1

class treeNodeAdv(T.TreeNode):
    def __init__(self, val):
        T.TreeNode.__init__(self, val)
        self.numberLeftChilds = 0


   #            0
   #          /    \
   #        1        2
   #      /        /   \
   #    3         4     5
   #  /   \
   # 6     7
treeNodeList = []
for i in range(8):
    treeNodeList.append(treeNodeAdv(i))
treeNodeList[0].leftChild = treeNodeList[1]
treeNodeList[0].rightChild = treeNodeList[2]
treeNodeList[1].leftChild = treeNodeList[3]
treeNodeList[2].leftChild = treeNodeList[4]
treeNodeList[2].rightChild = treeNodeList[5]
treeNodeList[3].leftChild = treeNodeList[6]
treeNodeList[3].rightChild = treeNodeList[7]
countNumberOfNodesInLeftSubtree(treeNodeList[0])
for treeNode in treeNodeList:
    print(treeNode.numberLeftChilds, end=' ')
print()
# -----------------------------------------------------------------------------------
maximumDifferenceBetweenLeftAndRightSubtree = 0
treeNodeWithMaxDifference = None
def findMaxDifferenceBetweenLeftAndRightSubtree(root):
    if root == None:
        return 0
    numOfNodesOnLeft = findMaxDifferenceBetweenLeftAndRightSubtree(root.leftChild)
    numOfNodesOnRight = findMaxDifferenceBetweenLeftAndRightSubtree(root.rightChild)
    global maximumDifferenceBetweenLeftAndRightSubtree, treeNodeWithMaxDifference
    if abs(numOfNodesOnRight - numOfNodesOnLeft) > maximumDifferenceBetweenLeftAndRightSubtree:
        maximumDifferenceBetweenLeftAndRightSubtree = abs(numOfNodesOnRight - numOfNodesOnLeft)
        treeNodeWithMaxDifference = root
    return numOfNodesOnLeft + numOfNodesOnRight + 1

findMaxDifferenceBetweenLeftAndRightSubtree(treeNodeList[0])
print(treeNodeWithMaxDifference.value, maximumDifferenceBetweenLeftAndRightSubtree)
# -----------------------------------------------------------------------------------
def findLowestCommonAncester1(root, targetNode1, targetNode2):
    if root == None or root == targetNode1 or root == targetNode2:
        return root
    findInLeft = findLowestCommonAncester1(root.leftChild, targetNode1, targetNode2)
    findInRight = findLowestCommonAncester1(root.rightChild, targetNode1, targetNode2)
    if findInLeft == None and findInRight == None:
        return None
    elif findInRight == None and findInLeft != None:
        return findInLeft
    elif findInLeft == None and findInRight != None:
        return findInRight
    else:
        return root

def findLowestCommonAncester2(root, targetNode, path):
    if root == None:
        return None
    if root == targetNode:
        path.append(root)
        return path
    path.append(root)
    leftPath = findLowestCommonAncester2(root.leftChild, targetNode, path)
    if leftPath != None:
        return leftPath
    rightPath = findLowestCommonAncester2(root.rightChild, targetNode, path)
    if rightPath != None:
        return rightPath
    path.pop()
    return None

print(findLowestCommonAncester1(treeNodeList[0], treeNodeAdv(10), treeNodeList[5]).value)

path1 = findLowestCommonAncester2(treeNodeList[0], treeNodeList[5], [])
path2 = findLowestCommonAncester2(treeNodeList[0], treeNodeList[4], [])
for index in range(len(path1)):
    if path1[index] != path2[index]:
        break
    index += 1
print(path1[index - 1].value)


