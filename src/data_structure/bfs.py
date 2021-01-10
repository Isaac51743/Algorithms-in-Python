import tree as t
import data_structure1 as ds1
import heapq as hq


def bfs1(root):
    if not root:
        return
    queue = ds1.Queue()
    queue.push(root)
    while not queue.is_empty():
        level_size = queue.get_size()
        for i in range(level_size):
            temp = queue.pop()
            if temp.left_child:
                queue.push(temp.left_child)
            if temp.right_child:
                queue.push(temp.right_child)
            print(temp.value, end=' ')
        print()


bfs1(t.test_root3)


def is_bipartite(root):
    if not root:
        return True
    queue = ds1.Queue()
    pre = {root}
    cur = set()
    visited = set()
    queue.push(root)
    while not queue.is_empty():
        level_size = queue.get_size()
        for i in range(level_size):
            temp = queue.pop()
            visited.add(temp)
            if temp.left_child and temp.left_child not in visited:
                if temp.left_child in pre:
                    return False
                cur.add(temp.left_child)
                queue.push(temp.left_child)

            if temp.right_child and temp.right_child not in visited:
                if temp.right_child in pre:
                    return False
                cur.add(temp.left_child)
                queue.push(temp.right_child)
        cur, pre = pre, cur
    return True


print(is_bipartite(t.test_root3))


def is_complete_tree(root):
    if not root:
        return True
    queue = ds1.Queue()
    queue.push(root)
    bubble_existed = False
    while not queue.is_empty():
        temp = queue.pop()
        # if not temp.left_child or temp.right_child:
        #     return False
        # if last_parent_passed and (temp.left_child or temp.right_child):
        #     return False

        if temp.left_child:
            if bubble_existed:
                return False
            queue.push(temp.left_child)
        else:
            bubble_existed = True

        if temp.right_child:
            if bubble_existed:
                return False
            queue.push(temp.right_child)
        else:
            bubble_existed = True
    return True


print(is_complete_tree(t.test_root3))


def find_kth_smallest_of_sorted_matrix(matrix, k):
    if len(matrix) == 0 or len(matrix[0]) == 0 or k <= 0:
        return None
    visited = {(0, 0)}
    heap = [(matrix[0][0], 0, 0)]
    count = 0
    while len(heap) > 0:
        temp = hq.heappop(heap)
        count += 1
        if count == k:
            return temp[0]
        if (temp[1] + 1, temp[2]) not in visited:
            hq.heappush(heap, (matrix[temp[1] + 1][temp[2]], temp[1] + 1, temp[2]))
            visited.add((temp[1] + 1, temp[2]))
        if (temp[1], temp[2] + 1) not in visited:
            hq.heappush(heap, (matrix[temp[1]][temp[2] + 1], temp[1], temp[2] + 1))
            visited.add((temp[1], temp[2] + 1))


testMatrix = [[2, 6, 8, 10], [4, 7, 10, 12], [7, 10, 11, 14], [9, 11, 13, 15]]
print(find_kth_smallest_of_sorted_matrix(testMatrix, 4))
