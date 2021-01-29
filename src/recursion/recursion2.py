import data_structure2 as ds2
import tree as t
print('Recursion2:')


def reverse_pair(head):
    if not head or not head.next:
        return head
    temp_next = reverse_pair(head.next.next)
    new_head = head.next
    head.next = temp_next
    new_head.next = head
    return new_head


test_head = ds2.ListNode(6)
cur_node = test_head
for i in range(4):
    cur_node.next = ds2.ListNode(5 - i)
    cur_node = cur_node.next
ds2.linked_list_print(test_head)
ds2.linked_list_print(reverse_pair(test_head))


def abbrev_match(text, abbrev, idx_text, idx_abbrev):
    if idx_text == len(text) and idx_abbrev == len(abbrev):
        return True
    elif idx_text == len(text) or idx_abbrev == len(abbrev):
        return False
    if abbrev[idx_abbrev].isdigit():
        count = 0
        while idx_abbrev < len(abbrev) and abbrev[idx_abbrev].isdigit():
            count = count * 10 + int(abbrev[idx_abbrev])
            idx_abbrev += 1
        idx_text += count
        if idx_text > len(text):
            return False
    elif text[idx_text] != abbrev[idx_abbrev]:
        return False
    else:
        idx_text += 1
        idx_abbrev += 1
    return abbrev_match(text, abbrev, idx_text, idx_abbrev)


test_text = 'this code is soooooo perfect like an art.'
abbrev = 't11 s6 perfect l10.'
print(abbrev_match(test_text, abbrev, 0, 0))


# edge length must > 3
def n_queen(pre_cols, slash, back_slash, result, edge_length):
    if len(pre_cols) == edge_length:
        print(result)
        return
    cur_row = len(pre_cols)
    for col in range(edge_length):
        if cur_row + col not in slash and cur_row - col not in back_slash and col not in pre_cols:
            result.append(col)
            pre_cols.add(col)
            slash.add(cur_row + col)
            back_slash.add(cur_row - col)
            n_queen(pre_cols, slash, back_slash, result, edge_length)
            result.pop()
            pre_cols.remove(col)
            slash.remove(cur_row + col)
            back_slash.remove(cur_row - col)


print("n queens: ")
n_queen(set(), set(), set(), [], 4)


def spiral_fill_matrix(matrix, cur_layer, count):
    if not matrix or not matrix[0]:
        return
    if cur_layer == (len(matrix) + 1) // 2:
        return
    edge_length = len(matrix) - 2 * cur_layer
    if edge_length > 1:
        for i in range(edge_length - 1):
            matrix[cur_layer][cur_layer + i] = count
            count += 1
        for i in range(edge_length - 1):
            matrix[cur_layer + i][cur_layer + edge_length - 1] = count
            count += 1
        for i in range(edge_length - 1):
            matrix[cur_layer + edge_length - 1][cur_layer + edge_length - 1 - i] = count
            count += 1
        for i in range(edge_length - 1):
            matrix[cur_layer + edge_length - 1 - i][cur_layer] = count
            count += 1
    else:
        matrix[cur_layer][cur_layer] = count
    spiral_fill_matrix(matrix, cur_layer + 1, count)


edge_length = 4
test_matrix = [[0] * edge_length for _ in range(edge_length)]
spiral_fill_matrix(test_matrix, 0, 0)
print("spiral fill matrix: ")
for row in range(len(test_matrix)):
    print(test_matrix[row])


def count_left_subtree(root):
    if not root:
        return 0
    left_num = count_left_subtree(root.left_child)
    right_num = count_left_subtree(root.right_child)
    root.left_num = left_num
    return left_num + right_num + 1


#            0
#          /    \
#        1        2
#      /        /   \
#    3         4     5
#  /   \
# 6     7
tree_node_list = []
for i in range(8):
    tree_node_list.append(t.TreeNode(i))
tree_node_list[0].left_child = tree_node_list[1]
tree_node_list[0].right_child = tree_node_list[2]
tree_node_list[1].left_child = tree_node_list[3]
tree_node_list[2].left_child = tree_node_list[4]
tree_node_list[2].right_child = tree_node_list[5]
tree_node_list[3].left_child = tree_node_list[6]
tree_node_list[3].right_child = tree_node_list[7]
count_left_subtree(tree_node_list[0])
for node in tree_node_list:
    print(node.left_num, end=' ')
print()


def find_node_max_difference(root):
    if not root:
        return 0
    left_num = find_node_max_difference(root.left_child)
    right_num = find_node_max_difference(root.right_child)
    global max_difference, node_max_difference
    if abs(left_num - right_num) > max_difference:
        max_difference = abs(left_num - right_num)
        node_max_difference = root
    return left_num + right_num + 1


max_difference = 0
node_max_difference = None
find_node_max_difference(tree_node_list[0])
print(node_max_difference.value, max_difference)


def lowest_common_ancestor1(root, node1, node2):
    if not root or root == node1 or root == node2:
        return root
    left = lowest_common_ancestor1(root.left_child, node1, node2)
    right = lowest_common_ancestor1(root.right_child, node1, node2)
    if left and right:
        return root
    elif left or right:
        return left if left else right
    else:
        return None


def lowest_common_ancestor2(root, target, path):
    if not root:
        return False
    elif root == target:
        path.append(target)
        return True
    path.append(root)
    find_in_left = lowest_common_ancestor2(root.left_child, target, path)
    find_in_right = lowest_common_ancestor2(root.right_child, target, path)
    if not find_in_left and not find_in_right:
        path.pop()
        return False
    return True


print(lowest_common_ancestor1(tree_node_list[0], tree_node_list[4], tree_node_list[3]).value)

path1 = []
path2 = []
lowest_common_ancestor2(tree_node_list[0], tree_node_list[5], path1)
lowest_common_ancestor2(tree_node_list[0], tree_node_list[4], path2)
index = 0
while index < len(path1) and index < len(path2):
    if path1[index] != path2[index]:
        break
    index += 1
if index > 0:
    print(path1[index - 1].value)
else:
    print("can't find common ancestor")


