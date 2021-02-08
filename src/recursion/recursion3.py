import tree as t
from collections import defaultdict
import data_structure2 as ds2

print("recursion3:")
#            4
#          /    \
#        3        5
#      /        /   \
#    1         6     7
#  /   \
# 0     2
tree_node_list = []
for i in range(8):
    tree_node_list.append(t.TreeNode(i))
tree_node_list[4].left_child = tree_node_list[3]
tree_node_list[4].right_child = tree_node_list[5]
tree_node_list[3].left_child = tree_node_list[1]
tree_node_list[1].left_child = tree_node_list[0]
tree_node_list[1].right_child = tree_node_list[2]
tree_node_list[5].left_child = tree_node_list[6]
tree_node_list[5].right_child = tree_node_list[7]


def is_balanced(root):
    if not root:
        return 0
    left_height = is_balanced(root.left_child)
    right_height = is_balanced(root.right_child)
    if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


print('is balanced tree:', is_balanced(tree_node_list[0]) != -1)


def max_sum_leaf_leaf(root):
    if not root:
        return 0

    left_sum = max_sum_leaf_leaf(root.left_child)
    right_sum = max_sum_leaf_leaf(root.right_child)
    global max_leaf_leaf
    if root.left_child and root.right_child and max_leaf_leaf < root.value + left_sum + right_sum:
        max_leaf_leaf = root.value + left_sum + right_sum
    return max(left_sum, right_sum) + root.value


def max_sum_path(root):
    if not root:
        return 0
    left_sum = max(0, max_sum_path(root.left_child))
    right_sum = max(0, max_sum_path(root.right_child))
    global max_path
    if max_path < left_sum + right_sum + root.value:
        max_path = left_sum + right_sum + root.value
    return max(left_sum, right_sum) + root.value


tree_node_list[6].value = -10
tree_node_list[0].value = -10
max_leaf_leaf = float('-inf')
max_sum_leaf_leaf(tree_node_list[4])
print('sum of max path from leaf to leaf', max_leaf_leaf)

max_path = float('-inf')
max_sum_path(tree_node_list[5])
print('sum of max path in the tree', max_path)
tree_node_list[6].value = 6
tree_node_list[0].value = 0


def max_sum_root_leaf(root, prefix):
    if not root:
        return
    elif not root.left_child and not root.right_child:
        global max_leaf_root
        max_leaf_root = max(max_leaf_root, prefix + root.value)
    max_sum_root_leaf(root.left_child, prefix + root.value)
    max_sum_root_leaf(root.right_child, prefix + root.value)


max_leaf_root = float('-inf')
tree_node_list[0].value = tree_node_list[1].value = tree_node_list[2].value = -10
max_sum_root_leaf(tree_node_list[3], 0)
print("max sum from root to leaf: ", max_leaf_root)
tree_node_list[0].value = 0
tree_node_list[1].value = 1
tree_node_list[2].value = 2
#            4
#          /    \
#        3        5
#      /        /   \
#    1         6     7
#  /   \
# 0     2


def target_sum_leaf_root(root, pre_values, target):
    if root is None:
        return
    pre_values.append(root.value)
    temp_sum = 0
    for i in range(1, len(pre_values) + 1):
        temp_sum += pre_values[-i]
        if temp_sum == target:
            global target_existed
            target_existed = True
            break
    target_sum_leaf_root(root.left_child, pre_values, target)
    target_sum_leaf_root(root.right_child, pre_values, target)
    pre_values.pop()


def target_sum_leaf_root_adv(root, prefix, prefix_dict, target):
    if root is None:
        return
    if prefix_dict[prefix + root.value - target] > 0 or prefix + root.value == target:
        global target_existed
        target_existed = True
    prefix_dict[prefix + root.value] += 1
    target_sum_leaf_root_adv(root.left_child, prefix + root.value, prefix_dict, target)
    target_sum_leaf_root_adv(root.right_child, prefix + root.value, prefix_dict, target)
    prefix_dict[prefix + root.value] -= 1


target_existed = False
target_sum_leaf_root(tree_node_list[4], [], 3)
print("target existed: ", target_existed)
target_existed = False
target_sum_leaf_root_adv(tree_node_list[4], 0, defaultdict(int), 13)
print("target existed: ", target_existed)


def max_sum_single_path(root, prefix):
    if root is None:
        return
    if prefix <= 0:
        new_prefix = root.value
    else:
        new_prefix = root.value + prefix
    global max_single_path
    max_single_path = max(max_single_path, new_prefix)
    max_sum_single_path(root.left_child, new_prefix)
    max_sum_single_path(root.right_child, new_prefix)


def max_sum_single_path_adv(root):
    if root is None:
        return 0
    left = max(0, max_sum_single_path_adv(root.left_child))
    right = max(0, max_sum_single_path_adv(root.right_child))
    global max_single_path_adv
    max_single_path_adv = max(max_single_path_adv, max(left, right) + root.value)
    return max(left, right) + root.value


max_single_path = max_single_path_adv = float("-inf")
max_sum_single_path(tree_node_list[4], 0)
max_sum_single_path_adv(tree_node_list[3])
print(max_single_path, max_single_path_adv)


def tree_doubly_list(root):
    if root is None:
        return
    tree_doubly_list(root.left_child)
    global list_tail
    list_tail.next = ds2.ListNode(root.value)
    list_tail.next.pre = list_tail
    list_tail = list_tail.next
    tree_doubly_list(root.right_child)


dummy = list_tail = ds2.ListNode(0)
tree_doubly_list(tree_node_list[4])
ds2.linked_list_print(dummy.next)


def preorder_tree(preorder, l_preorder, r_preorder, inorder, l_inorder, r_inorder, inorder_dict):
    if l_inorder > r_inorder:
        return None
    root = t.TreeNode(preorder[l_preorder])
    left_size = inorder_dict[preorder[l_preorder]] - l_inorder
    root.left_child = preorder_tree(preorder, l_preorder + 1, l_preorder + left_size, inorder, l_inorder, l_inorder + left_size - 1, inorder_dict)
    root.right_child = preorder_tree(preorder, l_preorder + left_size + 1, r_preorder, inorder, l_inorder + left_size + 1, r_inorder, inorder_dict)
    return root


inorder_array = [3, 2, 1]
preorder_array = [1, 2, 3]
inorder_dict = {}
for index in range(len(inorder_array)):
    inorder_dict[inorder_array[index]] = index


test_root1 = preorder_tree(preorder_array, 0, len(preorder_array) - 1, inorder_array, 0, len(preorder_array) - 1, inorder_dict)
t.in_order(test_root1)
print()
t.pre_order(test_root1)
print()

# def levelorderToTree(levelorderArray, inorderArray, leftIndexInorder, rightIndexInorder, inorderDictionary):
#     if leftIndexInorder > rightIndexInorder:
#         return None
#     root = T.TreeNode(levelorderArray[0])
#     leftSize = inorderDictionary[levelorderArray[0]] - leftIndexInorder
#     leftLevelorder = []
#     rightLevelorder = []
#     for index in range(1, len(levelorderArray)):
#         if inorderDictionary[levelorderArray[index]] < inorderDictionary[levelorderArray[0]]:
#             leftLevelorder.append(levelorderArray[index])
#         else:
#             rightLevelorder.append(levelorderArray[index])
#     root.leftChild = levelorderToTree(leftLevelorder, inorderArray, 0, inorderDictionary[levelorderArray[0]] - 1, inorderDictionary)
#     root.rightChild = levelorderToTree(rightLevelorder, inorderArray, inorderDictionary[levelorderArray[0]] + 1, rightIndexInorder, inorderDictionary)
#     return root

# levelorderArray = [1, 2, 3]
# testRoot2 = levelorderToTree(levelorderArray, inorderArray, 0, len(inorderArray) - 1, inorderDictionaryOfIndex)
# T.inOrder(testRoot2)
# print()
# T.preOrder(testRoot2)
# print()

