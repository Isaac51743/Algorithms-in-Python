# no order
# def subsets(st, index, result):
#     if index == len(st):
#         if result == '':
#             print('empty')
#         else:
#             print(result)
#         return
#     # not add
#     subsets(st, index + 1, result)
#     # add
#     result = result + st[index]
#     subsets(st, index + 1, result)
# restri = left remain - right remain

# def parenthesis(length, result, restri):
#     if len(result) == length:
#         if restri == 0:
#             print(result)
#         return
#     # print([restri, length//2])
#     if restri < length//2:
#         result = result + '{'
#         parenthesis(length, result, restri + 1)
#         result = result[:-1]
#     if restri > 0:
#         result = result + '}'
#         parenthesis(length, result, restri - 1)
def parenthesis2(length, l, r, result):
    if l + r == length:
        print(result)
        return
    if l < length//2:
        result = result + '{'
        parenthesis2(length, l + 1, r, result)
        result = result[:-1]
    if l > r:
        result = result + '}'
        parenthesis2(length, l, r + 1, result)
# def coins(total, cointype, result, remain):
#     if remain == 0:
#         print(result)
#         return
#     if cointype == 1:
#         for i in range(remain // 25 + 1):
#             result[25] = i
#             coins(total, cointype + 1, result, remain - i * 25)
#             result[25] = 0
#     elif cointype == 2:
#         for i in range(remain // 10 + 1):
#             result[10] = i
#             coins(total, cointype + 1, result, remain - i * 10)
#             result[10] = 0
#     elif cointype == 3:
#         for i in range(remain // 5 + 1):
#             result[5] = i
#             coins(total, cointype + 1, result, remain - i * 5)
#             result[5] = 0
#     elif cointype == 4:
#         result[1] = remain
#         coins(total, cointype + 1, result, 0)
#         result[1] = 0
# def strings(remain, result):
#     if len(remain) == 0:
#         print(result)
#         return
#     for i in range(len(remain)):
#         result = result + remain[i]
#         strings(remain[:i] + remain[i + 1:], result)
#         result = result[:-1]
# def strings1(s, index):
#     if index == len(s):
#         print(s)
#         return
#     for j in range(index, len(s)):
#         s[index], s[j] = s[j], s[index]
#         strings1(s, index + 1)
#         s[index], s[j] = s[j], s[index]
# def circlenum(edges):
#     table = {}
#     for edge in edges:
#         if edge[0] not in table:
#             table[edge[0]] = [edge[1]]
#         else:
#             table[edge[0]].append(edge[1])
#     print(table)
#     visited = []
#     circles = []
#     def DFS(node, target, path):
#         if node == target:
#             tem = []
#             for i in path:
#                 tem.append(i)
#             circles.append(tem)
#             visited.extend(path)
#             return
#         for item in table[node]:
#             # adding 'and item not in visited' means one node only contribute to one circle
#             if item not in path:
#                 path.append(item)
#                 DFS(item, target, path)
#                 del path[-1]
#
#     for k in table:
#         if k not in visited:
#             for val in table[k]:
#                 DFS(val, k, [val])
#     print(circles)
#     print(len(circles))
# 4/9/2020
def subsets(st, indx, result):
    if indx == len(st):
        if result == '':
            print('empty', end = ' ')
        else:
            print(result, end = ' ')
        return
    subsets(st, indx + 1, result)
    result = result + st[indx]
    subsets(st, indx + 1, result)
def parenthesis(length, l, r, result):
    if len(result) == length:
        print(result, end = ' ')
        return
    if l < length//2:
        result += '{'
        parenthesis(length, l + 1, r, result)
        result = result[:-1]
    if l > r:
        result += '}'
        parenthesis(length, l, r + 1, result)
        result = result[:-1]
def coins(cointype, result, remain):
    if remain == 0:
        print(result)
        return
    if cointype == 1:
        for i in range(remain//25 + 1):
            result[25] = i
            coins(cointype + 1, result, remain - i * 25)
            result[25] = 0
    elif cointype == 2:
        for i in range(remain//10 + 1):
            result[10] = i
            coins(cointype + 1, result, remain - i * 10)
            result[10] = 0
    elif cointype == 3:
        for i in range(remain // 5 + 1):
            result[5] = i
            coins(cointype + 1, result, remain - i * 5)
            result[5] = 0
    elif cointype == 4:
        result[1] = remain
        coins(cointype + 1, result, 0)
        result[1] = 0
def strings(remain, result):
    if len(remain) == 0:
        print(result)
        return
    for i in range(len(remain)):
        result += remain[i]
        strings(remain[:i] + remain[i + 1:], result)
        result = result[:-1]
def strings1(s, index):
    if index == len(s):
        print(s)
        return
    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]
        strings1(s, index + 1)
        s[index], s[i] = s[i], s[index]
# assuming one node only contribute to one circle
def circlenumNEW(edges):
    table = {}
    for edge in edges:
        if edge[0] not in table:
            table[edge[0]] = [edge[1]]
        else:
            table[edge[0]].append(edge[1])
    print(table)
    # visited stores nodes that has been explored all circular path
    visited = []
    circlenum = 0
    def dfs(node, path):
        # print(path, end=' ')
        # print(node)
        if len(path) > 0 and node == path[0]:
            print(path)
            nonlocal circlenum
            circlenum += 1
            return
        for sub in table[node]:
                    # dont need to visit visted nodes and nodes already in the path
                    if sub not in path[1:] and sub not in visited:
                        dfs(sub, path + [node])
    for k in table:
        dfs(k, [])
        visited.append(k)
    print(circlenum)

s = 'abcd'
subsets(s, 0, '')
print()
# parenthesis(6, '', 0)
parenthesis(6, 0, 0, '')
# parenthesis2(6, 0, 0, '')
print()
# coins(1, {}, 99)
strings('abc','')
strings1(['a', 'b', 'c'], 0)
e = [('a', 'c'), ('c', 'e'), ('b', 'd'), ('d', 'a'), ('a', 'b'), ('e', 'f'), ('f', 'c'), ('a', 'a')]
circlenumNEW(e)