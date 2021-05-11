import bfs as B
print('Hash table:')
def findTopKFrequentWord(text, k):
    dictionary = {}
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('?', '')
    wordList = text.split(' ')
    for word in wordList:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    print(dictionary)
    heap = B.HeapAdv()
    for word in dictionary:
        if heap.getSize() < k:
            heap.insert([dictionary[word], word])
        else:
            if dictionary[word] > heap.getTop()[0]:
                heap.pop()
                heap.insert([dictionary[word], word])
    result = []
    while not heap.isEmpty():
        result.append(heap.pop()[1])
    return result

testText = 'i love you so much, but you do not love me. can you hug me a little bit?'
print(findTopKFrequentWord(testText, 3))

def findMissingNum1(array):
    hashset = set()
    for number in array:
        hashset.add(number)
    result = []
    for number in range(min(array), max(array) + 1):
        if number not in hashset:
            result.append(number)
    return result

def findMissingNum2(array): # assuming only one missing number
    total = (min(array) + max(array)) * (max(array) - min(array) + 1) //2
    for number in array:
        total = total - number
    return total

def findMissingNum3(array): # assuming only one missing number
    result = 0
    for number in array:
        result = result ^ number
    for number in range(min(array), max(array) + 1):
        result = result ^ number
    return result

testList1 = [3, 2, 7, 4, 10, 6, 9, 8]
print(findMissingNum3(testList1))


def findCommonNumbersBetween2SortedLists1(array1, array2):
    if len(array1) == 0 or len(array2) == 0:
        return None
    hashset = set()
    result = set()
    if len(array1) > len(array2):
        for number in array2:
            hashset.add(number)
        for number in array1:
            if number in hashset:
                result.add(number)
    else:
        for number in array1:
            hashset.add(number)
        for number in array2:
            if number in hashset:
                result.add(number)
    return result


def findCommonNumbersBetween2SortedLists2(array1, array2):
    if len(array1) == 0 or len(array2) == 0:
        return None
    result = set()
    index1 = 0
    index2 = 0
    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] < array2[index2]:
            index1 += 1
        elif array1[index1] > array2[index2]:
            index2 += 1
        else:
            result.add(array1[index1])
            index1 += 1
            index2 += 1
    return result


testList2 = [1, 3, 5, 7, 8, 12, 24]
testList3 = [1, 3, 6, 7, 10, 12, 14]
print(findCommonNumbersBetween2SortedLists1(testList2, testList3))
print(findCommonNumbersBetween2SortedLists2(testList2, testList3))