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


def search_bst(root, target):
    if root is None:
        return None
    if root.value < target:
        return search_bst(root.right_child, target)
    elif root.value > target:
        return search_bst(root.left_child, target)
    else:
        return root


def insert_bst_recursion1(root, target):
    if root is None:
        return TreeNode(target)
    if root.value < target:
        root.right_child = insert_bst_recursion1(root.right_child, target)
    elif root.value > target:
        root.left_child = insert_bst_recursion1(root.left_child, target)
    return root


def insert_bst_iteration(root, target):
    if root is None:
        return TreeNode(target)
    pre = None
    cur = root
    while cur is not None:
        pre = cur
        if cur.value < target:
            cur = cur.right_child
        elif cur.value > target:
            cur = cur.left_child
        else:
            return root
    if pre.value < target:
        pre.right_child = TreeNode(target)
    else:
        pre.left_child = TreeNode(target)
    return root


def insert_bst_recursion2(root, target):
    if root is None:
        return TreeNode(target)
    helper(root, target)
    return root


def helper(root, target):
    if root.value > target:
        if root.left_child:
            helper(root.left_child, target)
        else:
            root.left_child = TreeNode(target)
    elif root.value < target:
        if root.right_child:
            helper(root.right_child, target)
        else:
            root.right_child = TreeNode(target)


def remove_bst(root, target):
    if root is None:
        return root
    if root.value < target:
        root.right_child = remove_bst(root.right_child, target)
        return root
    elif root.value > target:
        root.left_child = remove_bst(root.left_child, target)
        return root
    else:
        if root.left_child is None and root.right_child is None:
            return None
        elif root.left_child is None:
            return root.right_child
        elif root.right_child is None:
            return root.left_child
        else:
            if root.right.left is None:
                root.rihgt.left = root.left
                return root.right
            elif root.left.right is None:
                root.left.right = root.right
                return root.left
            else:
                min_in_right = remove_min(root.right)
                min_in_right.left_child = root.left_child
                min_in_right.right_child = root.right_child
                return min_in_right


def remove_min(root):
    if root is None or root.left_child is None:
        return None
    pre = root
    cur = root.left_child
    while cur.left_child:
        pre = cur
        cur = cur.left_child
    pre.left_child = cur.right_child
    return cur


def pre_order_iteration(root):
    if root is None:
        return
    stack = [root]
    while len(stack) > 0:
        temp = stack.pop()
        print(temp.value, end=" ")
        if temp.right_child:
            stack.append(temp.right_child)
        if temp.left_child:
            stack.append(temp.left_child)
    return


def in_order_iteration(root):
    if root is None:
        return []
    next_to_visit = root
    stack = []
    while len(stack) > 0 or next_to_visit:
        if next_to_visit is None:
            temp = stack.pop()
            print(temp.value, end=" ")
            next_to_visit = temp.right_child
        else:
            stack.append(next)
            next_to_visit = next_to_visit.left_child



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

