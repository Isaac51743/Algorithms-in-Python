import data_structure1 as ds1


class TreeNode(object):

    def __init__(self, value=-1, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def add_left(self, node):
        self.left_child = node

    def add_right(self, node):
        self.right_child = node


test_root1 = TreeNode(1)
test_root1.add_left(TreeNode(2))
test_root1.add_right(TreeNode(3))
test_root2 = TreeNode(1)
test_root2.add_left(TreeNode(3))
test_root2.add_right(TreeNode(2))
test_root3 = TreeNode(10)
test_root3.add_left(TreeNode(3))
test_root3.add_right(TreeNode(12))
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


def pre_order(root):
    if not root:
        return
    print(root.value, end=' ')
    pre_order(root.left_child)
    pre_order(root.right_child)


def in_order(root):
    if not root:
        return
    in_order(root.left_child)
    print(root.value, end=' ')
    in_order(root.right_child)


def post_order(root):
    if not root:
        return
    post_order(root.left_child)
    post_order(root.right_child)
    print(root.value, end=' ')


def get_height(root):
    if not root:
        return 0
    left_height = get_height(root.left_child)
    right_height = get_height(root.right_child)
    return max(left_height, right_height) + 1


def is_balanced(root):
    if not root:
        return True
    left_height = get_height(root.left_child)
    right_height = get_height(root.right_child)
    if abs(left_height - right_height) <= 1 and is_balanced(root.left_child) and is_balanced(root.right_child):
        return True
    else:
        return False


def is_symmetric(left_node, right_node):
    if not left_node and not right_node:
        return True
    elif not left_node or not right_node or left_node.value != right_node.value:
        return False
    return is_symmetric(left_node.left_child, right_node.right_child) and \
           is_symmetric(left_node.right_child, right_node.left_child)


def is_identical(left_node, right_node):
    if not left_node and not right_node:
        return True
    elif not left_node or not right_node or left_node.value != right_node.value:
        return False
    case1 = is_identical(left_node.left_child, right_node.right_child) and \
        is_identical(left_node.right_child, right_node.left_child)
    case2 = is_identical(left_node.right_child, right_node.left_child) and \
        is_identical(left_node.left_child, right_node.right_child)
    return case1 or case2


def is_bst(root, small_bound, big_bound):
    if not root:
        return True
    elif root.value <= small_bound or root.value >= big_bound:
        return False
    return is_bst(root.left_child, small_bound, root.value) and is_bst(root, root.value, big_bound)


def in_order_in_range(root, small_bound, big_bound):
    if not root:
        return
    if root.value > small_bound:
        in_order_in_range(root.left_child, small_bound, big_bound)
    if big_bound >= root.value >= small_bound:
        print(root.value, end=' ')
    if root.value < big_bound:
        in_order_in_range(root.right_child, small_bound, big_bound)


# def searchBST(root, target):
#     if root == None or root.value == target:
#         return root
#     if root.value > target:
#         return searchBST(root.leftChild, target)
#     else:
#         return searchBST(root.rightChild, target)
#
# def insertBSTRecursion1(root, target):
#     if root == None:
#         return TreeNode(target)
#     if root.value > target:
#         root.leftChild = insertBSTRecursion1(root.leftChild, target)
#     elif root.value < target:
#         root.rightChild = insertBSTRecursion1(root.rightChild, target)
#     return root
#
# def insertBSTIteration1(root, target):
#     if root == None:
#         return TreeNode(target)
#     preNode = None
#     curNode = root
#     while curNode != None:
#         preNode = curNode
#         if curNode.value > target:
#             curNode = curNode.leftChild
#         elif curNode.value < target:
#             curNode = curNode.rightChild
#         else:
#             return root
#     if preNode.value > target:
#         preNode.leftChild = TreeNode(target)
#     elif preNode.value < target:
#         preNode.rightChild = TreeNode(target)
#     return root
#
# def insertBSTRecursion2(root, target):
#     if root == None:
#         return TreeNode(target)
#     helper(root, target)
#     return root
# def helper(root, target):
#     if root.value > target:
#         if root.leftChild != None:
#             helper(root.leftChild, target)
#         else:
#             root.leftChild = TreeNode(target)
#     elif root.value < target:
#         if root.rightChild != None:
#             helper(root.rightChild, target)
#         else:
#             root.rightChild = TreeNode(target)
#
# def insertBSTIteration2(root, target):
#     if root == None:
#         return TreeNode(target)
#     curNode = root
#     while curNode.value != target:
#         if curNode.value < target:
#             if curNode.rightChild != None:
#                 curNode = curNode.rightChild
#             else:
#                 curNode.rightChild = TreeNode(target)
#                 break
#         elif curNode.value > target:
#             if curNode.leftChild != None:
#                 curNode = curNode.leftChild
#             else:
#                 curNode.leftChild = TreeNode(target)
#                 break
#     return root
# def removeBST(root, target):
#     if root == None:
#         return None
#     if target < root.value:
#         root.leftChild = removeBST(root.leftChild, target)
#     elif target > root.value:
#         root.rightChild = removeBST(root.rightChild, target)
#     else:
#         if root.leftChild == None:
#             return root.rightChild
#         elif root.rightChild == None:
#             return root.leftChild
#         else:
#             if root.rightChild.leftChild == None:
#                 root.rightChild.leftChild = root.leftChild
#                 return root.right
#             else:
#                 smallestOnRight = deleteMin(root.rightChild)
#                 smallestOnRight.leftChild = root.leftChild
#                 smallestOnRight.rightChild = root.rightChild
#                 return smallestOnRight
#     return root
# # assuming root must has left child
# def deleteMin(root):
#     preNode = root
#     curNode = root.leftChild
#     while curNode != None:
#         preNode = curNode
#         curNode = curNode.leftChild
#     preNode.leftChild = curNode.rightChild
#     return curNode
#
# print(searchBST(testRoot3, 10))
# newRoot3 = insertBSTRecursion2(testRoot3, 1)
# print(searchBST(newRoot3, 1))
# newRoot3 = insertBSTIteration2(newRoot3, 2)
# print(searchBST(newRoot3, 2))
# newRoot3 = removeBST(newRoot3, 1)
# print(searchBST(newRoot3, 1))
# #------------------------------------------------------------------------------------
# def preOrderIteration(root):
#     if root == None:
#         return
#     stack = DS1.Stack()
#     stack.push(root)
#     while not stack.isEmpty():
#         curNode = stack.pop()
#         print(curNode.value, end=' ')
#         if curNode.rightChild != None:
#             stack.push(curNode.rightChild)
#         if curNode.leftChild != None:
#             stack.push(curNode.leftChild)
#
# def inOrderIteration(root):
#     if root == None:
#         return
#     stack = DS1.Stack()
#     nextNode = root
#     while not stack.isEmpty() or nextNode != None:
#         if nextNode != None:
#             stack.push(nextNode)
#             nextNode = nextNode.leftChild
#         else: # top element is the stack has no left child any more
#             curNode = stack.pop()
#             print(curNode.value, end=' ')
#             nextNode = curNode.rightChild
#
# def postOrderIteration(root):
#     if root == None:
#         return
#     preNode = None
#     stack = DS1.Stack()
#     stack.push(root)
#     while not stack.isEmpty():
#         curNode = stack.getTop()
#         if preNode == None or preNode.leftChild == curNode or preNode.rightChild == curNode:
#             if curNode.leftChild != None:
#                 stack.push(curNode.leftChild)
#             elif curNode.rightChild != None:
#                 stack.push(curNode.rightChild)
#             else:
#                 print(stack.pop().value, end=' ')
#         elif curNode.leftChild == preNode:
#             if curNode.rightChild != None:
#                 stack.push(curNode.rightChild)
#             else:
#                 print(stack.pop().value, end=' ')
#         else:
#             print(stack.pop().value, end=' ')
#         preNode = curNode
#
# preOrderIteration(testRoot3)
# print()
# inOrderIteration(testRoot3)
# print()
# postOrderIteration(testRoot3)
# print()

