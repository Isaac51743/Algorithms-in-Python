def findAllSubset(word, curIndex, result):
    if curIndex == len(word):
        if len(result) == 0:
            print('None', end=' ')
        else:
            print(''.join(result), end=' ')
        return
    findAllSubset(word, curIndex + 1, result)
    result.append(word[curIndex])
    findAllSubset(word, curIndex + 1, result)
    result.pop()

word = 'domi'
findAllSubset(word, 0, [])
print()

def permutationOfParenthesis(leftParenthesisLeft, rightParenthesisLeft, result):
    if leftParenthesisLeft == 0 and rightParenthesisLeft == 0:
        print(''.join(result), end=' ')
        return
    if leftParenthesisLeft > 0:
        result.append('{')
        permutationOfParenthesis(leftParenthesisLeft - 1, rightParenthesisLeft, result)
        result.pop()
    if leftParenthesisLeft < rightParenthesisLeft:
        result.append('}')
        permutationOfParenthesis(leftParenthesisLeft, rightParenthesisLeft - 1, result)
        result.pop()

permutationOfParenthesis(3, 3, [])
print()

def allCombinationOfCoin(coinType, curIndex, remainAmount, combination):
    if curIndex == len(coinType):
        if remainAmount == 0:
            print(combination)
            return
        else:
            return
    curCoin =coinType[curIndex]
    coinNumber = remainAmount // curCoin
    for number in range(coinNumber + 1):
        combination[curCoin] = number
        allCombinationOfCoin(coinType, curIndex + 1, remainAmount - number * curCoin, combination)

coinType = [8, 4, 2]
allCombinationOfCoin(coinType, 0, 10, {})

def permutationOfString1(letterList, curIndex):
    if curIndex == len(letterList):
        print(''.join(letterList), end=' ')
        return
    for index in range(curIndex, len(letterList)):
        letterList[curIndex], letterList[index] = letterList[index], letterList[curIndex]
        permutationOfString1(letterList, curIndex + 1)
        letterList[curIndex], letterList[index] = letterList[index], letterList[curIndex]

def permutationOfString2(letterList, visitedIndex, result):
    if len(visitedIndex) == len(letterList):
        print(''.join(result), end=' ')
        return
    for index in range(len(letterList)):
        if index not in visitedIndex:
            visitedIndex.add(index)
            result.append(letterList[index])
            permutationOfString2(letterList, visitedIndex, result)
            result.pop()
            visitedIndex.remove(index)

letterList = list('abc')
permutationOfString1(letterList, 0)
print()
permutationOfString2(letterList, set(), [])
print()

# assuming one node only contribute to one circle
def circleNumber(edges):
    table = {}
    for edge in edges:
        if edge[0] not in table:
            table[edge[0]] = [edge[1]]
        else:
            table[edge[0]].append(edge[1])
    # 'visited' stores nodes that has been explored all circular path
    visitedNode = set()
    circleNum = 0
    def dfs(node, path):
        if len(path) > 0 and node == path[0]:
            nonlocal circleNum
            circleNum += 1
            return
        for nextNode in table[node]:
            # don't need to visit visted nodes and nodes already in the path
            if nextNode not in path[1:] and nextNode not in visitedNode:
                path.append(node)
                dfs(nextNode, path)
                path.pop()
    for node in table:
        dfs(node, [])
        visitedNode.add(node)
    print(circleNum)

e = [('a', 'c'), ('c', 'e'), ('b', 'd'), ('d', 'a'), ('a', 'b'), ('e', 'f'), ('f', 'c'), ('a', 'a')]
circleNumber(e)