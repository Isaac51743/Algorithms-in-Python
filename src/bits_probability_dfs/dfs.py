def find_all_subset(word, cur_index, result):
    if cur_index == len(word):
        if len(result) == 0:
            print('None', end=' ')
        else:
            print(''.join(result), end=' ')
        return
    find_all_subset(word, cur_index + 1, result)
    result.append(word[cur_index])
    find_all_subset(word, cur_index + 1, result)
    result.pop()


def permutation_of_parenthesis1(pair_num, left, right, result):
    if left + right == 2 * pair_num:
        print(''.join(result), end=' ')
        return
    if left < pair_num:
        result.append('(')
        permutation_of_parenthesis1(pair_num, left + 1, right, result)
        result.pop()
    if right < left:
        result.append(')')
        permutation_of_parenthesis1(pair_num, left, right + 1, result)
        result.pop()


def permutation_of_parenthesis2(left_parenthesis_left, right_parenthesis_left, result):
    if left_parenthesis_left == 0 and right_parenthesis_left == 0:
        print(''.join(result), end=' ')
        return
    if left_parenthesis_left > 0:
        result.append('{')
        permutation_of_parenthesis2(left_parenthesis_left - 1, right_parenthesis_left, result)
        result.pop()
    if left_parenthesis_left < right_parenthesis_left:
        result.append('}')
        permutation_of_parenthesis2(left_parenthesis_left, right_parenthesis_left - 1, result)
        result.pop()


def all_combination_of_coin(coin_types, cur_index, remain_amount, combination):
    if cur_index == len(coin_types):
        if remain_amount == 0:
            print(combination)
        return

    cur_coin = coin_types[cur_index]
    coin_number = remain_amount // cur_coin
    for number in range(coin_number + 1):
        combination[cur_coin] = number
        all_combination_of_coin(coin_types, cur_index + 1, remain_amount - number * cur_coin, combination)


def permutation_of_string1(letter_list, cur_index):
    if cur_index == len(letter_list):
        print(''.join(letter_list), end=' ')
        return
    for index in range(cur_index, len(letter_list)):
        letter_list[cur_index], letter_list[index] = letter_list[index], letter_list[cur_index]
        permutation_of_string1(letter_list, cur_index + 1)
        letter_list[cur_index], letter_list[index] = letter_list[index], letter_list[cur_index]


def permutation_of_string2(letter_list, visited_index, result):
    if len(visited_index) == len(letter_list):
        print(''.join(result), end=' ')
        return
    for index in range(len(letter_list)):
        if index not in visited_index:
            visited_index.add(index)
            result.append(letter_list[index])
            permutation_of_string2(letter_list, visited_index, result)
            result.pop()
            visited_index.remove(index)


# assuming one node only contribute to one circle
def find_circle_number(edges):
    table = {}
    for edge in edges:
        if edge[0] not in table:
            table[edge[0]] = [edge[1]]
        else:
            table[edge[0]].append(edge[1])
    # 'visited' stores nodes that has been explored all circular path
    visited_node = set()
    circle_num = 0

    def dfs(cur_node, path):
        if len(path) > 0 and cur_node == path[0]:
            nonlocal circle_num
            circle_num += 1
            return
        for next_node in table[cur_node]:
            # don't need to visit visted nodes and nodes already in the path
            if next_node not in path[1:] and next_node not in visited_node:
                path.append(cur_node)
                dfs(next_node, path)
                path.pop()

    for node in table:
        dfs(node, [])
        visited_node.add(node)
    print(visited_node)


test_word = 'domi'
find_all_subset(test_word, 0, [])
print()
permutation_of_parenthesis1(3, 0, 0, [])
print()
permutation_of_parenthesis2(3, 3, [])
print()
test_coin_types = [8, 4, 1]
all_combination_of_coin(test_coin_types, 0, 10, {})
test_letter_list = list('abc')
permutation_of_string1(test_letter_list, 0)
print()
permutation_of_string2(test_letter_list, set(), [])
print()
test_edges = [('a', 'c'), ('c', 'e'), ('b', 'd'), ('d', 'a'), ('a', 'b'), ('e', 'f'), ('f', 'c'), ('a', 'a')]
find_circle_number(test_edges)