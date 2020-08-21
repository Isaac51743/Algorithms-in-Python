import collections


def search_matrix(self, matrix, target):
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    m, n = len(matrix), len(matrix[0])

    pivot = [m - 1, 0]

    while pivot[0] >= 0 and pivot[1] < n:
        if matrix[pivot[0]][pivot[1]] == target:
            return True
        elif matrix[pivot[0]][pivot[1]] < target:
            pivot[1] += 1
        else:
            pivot[0] -= 1

    return False


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _is_same(self, root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    elif root1.val != root2.val:
        return False
    return self._is_same(root1.left, root2.left) and self._is_same(root1.right, root2.right)


def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
    if self._is_same(s, t):
        return True
    if s.left and self.isSubtree(s.left, t):
        return True
    if s.right and self.isSubtree(s.right, t):
        return True
    return False


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def deep_copy_linklist(head):
    if head is None:
        return None
    original_dict = {}
    copy_list = []
    cur_pointer = head
    index = 0
    while cur_pointer:
        original_dict[cur_pointer] = index
        index += 1
        copy_list.append(Node(cur_pointer.val))
        cur_pointer = cur_pointer.next

    for i in range(len(copy_list) - 1):
        copy_list[i].next = copy_list[i + 1]

    cur_pointer = head
    for node in copy_list:
        if cur_pointer.random:
            node.random = copy_list[original_dict[cur_pointer.random]]
        cur_pointer = cur_pointer.next
    return copy_list[0]


def critical_connections(n: int, connections: list) -> list:
    def dfs(rank, curr, prev):
        lowest_rank_reachable[curr] = rank
        result = []
        for neighbor in graph[curr]:
            if neighbor != prev:
                if lowest_rank_reachable[neighbor] == 0:
                    result += dfs(rank + 1, neighbor, curr)
                lowest_rank_reachable[curr] = min(lowest_rank_reachable[curr], lowest_rank_reachable[neighbor])
                if lowest_rank_reachable[neighbor] == rank + 1:
                    result.append([curr, neighbor])
        return result

    lowest_rank_reachable = [0] * n  # except the comming path
    graph = collections.defaultdict(list)
    for [node1, node2] in connections:
        graph[node1].append(node2)
        graph[node2].append(node1)

    return dfs(1, 0, -1)


print(critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))


def find_pair_songs(durations, total_time, num_songs):
    index_dict = {}
    result_pair = (-1, -1)
    for i in range(num_songs):
        remain = total_time - durations[i]
        if remain in index_dict:
            temp_pair = (i, index_dict[remain]) if durations[i] < durations[index_dict[remain]] else (index_dict[remain], i)
            result_pair = temp_pair if result_pair[-1] == -1 or durations[temp_pair[-1]] > durations[result_pair[-1]] else result_pair
        else:
            index_dict[durations[i]] = i
    return result_pair


print(find_pair_songs([1, 10, 25, 35,  60], 60, 5))