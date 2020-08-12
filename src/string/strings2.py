def reverseRecursion(text, leftIndex, rightIndex):
    if leftIndex >= rightIndex:
        return ''.join(text)
    text[leftIndex], text[rightIndex] = text[rightIndex], text[leftIndex]
    return reverseRecursion(text, leftIndex + 1, rightIndex - 1)


def reverseIteration(text):
    if len(text) == 0:
        return text
    text = list(text)
    leftBound = 0
    rightBound = len(text) - 1
    while leftBound < rightBound:
        text[leftBound], text[rightBound] = text[rightBound], text[leftBound]
        leftBound += 1
        rightBound -= 1
    return ''.join(text)


def reverseWordOrder(text):
    if len(text) == 0:
        return text
    text = list(text)
    startIndex = 0
    while True:
        while startIndex < len(text) and text[startIndex] == ' ':
            startIndex += 1
        if startIndex == len(text):
            break
        endIndex = startIndex
        while endIndex < len(text) and text[endIndex] != ' ':
            endIndex += 1
        reverseRecursion(text, startIndex, endIndex - 1)
        startIndex = endIndex
    return reverseRecursion(text, 0, len(text) - 1)


testText1 = 'zhao yue hang'
print(reverseRecursion(list(testText1), 0, len(testText1) - 1))
print(reverseIteration(testText1))
print(reverseWordOrder(testText1))


def isSame(word1, word2):
    if len(word1) != len(word2):
        return False
    for index in range(len(word1)):
        if word1[index] != word2[index]:
            return False
    return True


def replacement(text, segment1, segment2):
    if len(text) == 0 or len(segment2) == 0:
        return text
    text = list(text)
    segment1 = list(segment1)
    segment2 = list(segment2)
    if len(segment1) >= len(segment2):
        slowPointer = fastPointer = 0
        while fastPointer < len(text):
            if fastPointer + len(segment1) - 1 < len(text) and isSame(text[fastPointer:fastPointer + len(segment1)], segment1):
                for index in range(len(segment2)):
                    text[slowPointer] = segment2[index]
                    slowPointer += 1
                fastPointer += len(segment1)
            else:
                text[slowPointer], text[fastPointer] = text[fastPointer], text[slowPointer]
                fastPointer += 1
                slowPointer += 1
        return ''.join(text[:slowPointer])
    else:
        index = 0
        occurence = 0
        while index + len(segment1) - 1 < len(text):
            if isSame(text[index:index + len(segment1)], segment1):
                occurence += 1
            index += 1
        fastPointer =len(text) - 1
        for i in range(occurence * (len(segment2) - len(segment1))):
            text.append(' ')
        slowPointer = len(text) - 1
        while fastPointer - len(segment1) + 1 >= 0:
            if isSame(text[fastPointer - len(segment1) + 1: fastPointer + 1], segment1):
                for index in range(len(segment2)):
                    text[slowPointer] = segment2[len(segment2) - index - 1]
                    slowPointer -= 1
                fastPointer -= len(segment1)
            else:
                text[slowPointer], text[fastPointer] = text[fastPointer] ,text[slowPointer]
                slowPointer -= 1
                fastPointer -= 1
        return ''.join(text)

testText2 = 'my name is hang, and all my friends like hang. hang is from my father.'
print(replacement(testText2, 'hang', 'zhaoyuehang'))
print(replacement(testText2, 'hang', 'ZYH'))


# the length of input text is always even
def shuffle(text, leftIndex, rightIndex):
    if rightIndex - leftIndex + 1 < 4:
        return
    length = rightIndex - leftIndex + 1
    startOfSubarray3 = leftIndex + length // 2
    startOfSubarray2 = leftIndex + length // 4
    startOfSubarray4 = startOfSubarray3 + length // 4
    reverseRecursion(text, startOfSubarray2, startOfSubarray3 - 1)
    reverseRecursion(text, startOfSubarray3, startOfSubarray4 - 1)
    reverseRecursion(text, startOfSubarray2, startOfSubarray4 - 1)
    shorterSubarrayLength = length // 4
    shuffle(text, leftIndex, leftIndex + 2 * shorterSubarrayLength - 1)
    shuffle(text, leftIndex + 2 * shorterSubarrayLength, rightIndex)

testText3 = list('abcdefg1234567')
shuffle(testText3, 0, len(testText3) - 1)
print(''.join(testText3))

def permutationOfText(text, startIndex):
    if len(text) == 0:
        print(''.join(text))
        return
    if startIndex == len(text):
        print(''.join(text), end=' ')
        return
    visited = set()
    for index in range(startIndex, len(text)):
        if text[index] not in visited:
            visited.add(text[index])
            text[startIndex], text[index] = text[index], text[startIndex]
            permutationOfText(text, startIndex + 1)
            text[startIndex], text[index] = text[index], text[startIndex]

testText4 = list('bacc')
permutationOfText(testText4, 0)
print()

def findLongestSubstringWithKZeros(text, k):
    if len(text) == 0 or k <= 0:
        return None
    leftBound = 0
    zerosCount = 0
    finalLeft = finalRight = -1
    for rightBound in range(len(text)):
        if text[rightBound] == '0':
            if zerosCount < k:
                zerosCount += 1
            else:
                while text[leftBound] != '0':
                    leftBound += 1
                leftBound += 1
        if rightBound - leftBound > finalRight - finalLeft:
            finalLeft = leftBound
            finalRight = rightBound
    if zerosCount < k:
        return None
    return text[finalLeft:finalRight + 1]

def findLongestSubstringWithUniqueLetter(text):
    if len(text) == 0:
        return text
    hashSet = set()
    leftBound = 0
    finalLeft = finalRight = 0
    for rightBound in range(len(text)):
        if text[rightBound] not in hashSet:
            hashSet.add(text[rightBound])
        else:
            while text[leftBound] != text[rightBound]:
                hashSet.remove(text[leftBound])
                leftBound += 1
            leftBound += 1
        if rightBound - leftBound > finalRight - finalLeft:
            finalLeft = leftBound
            finalRight = rightBound
    return text[finalLeft:finalRight + 1]

def findLongestSubstringWithKOccurrence(text, k):
    if len(text) == 0:
        return text
    if k <= 0:
        return None
    leftBound = 0
    hashTable = {}
    finalLeft = finalRight = 0
    for rightBound in range(len(text)):
        if text[rightBound] not in hashTable:
            hashTable[text[rightBound]] = 1
        else:
            if hashTable[text[rightBound]] < k:
                hashTable[text[rightBound]] += 1
            else:
                while text[leftBound] != text[rightBound]:
                    hashTable[text[leftBound]] -= 1
                    leftBound += 1
                leftBound += 1
        if rightBound - leftBound > finalRight - finalLeft:
            finalLeft = leftBound
            finalRight = rightBound
    return text[finalLeft:finalRight + 1]

testText5 = '0100101010111010101'
print(findLongestSubstringWithKZeros(testText5, 3))
testText6 = 'abcdebfghijklmn'
print(findLongestSubstringWithUniqueLetter(testText6))
print(findLongestSubstringWithKOccurrence(testText5, 2))

def isNumber(letter):
    if ord(letter) >= ord('0') and ord(letter) <= ord('9'):
        return True
    return False
def encodeString(text):
    if len(text) == 0:
        return text
    text = list(text)
    slowPointer = fastPointer = 0
    numberOfSingleLetter = 0
    while fastPointer < len(text):
        text[slowPointer] = text[fastPointer]
        slowPointer += 1
        numOfReplica = 0
        while fastPointer < len(text) and text[fastPointer] == text[slowPointer - 1]:
            numOfReplica += 1
            fastPointer += 1
        if numOfReplica > 1:
            text[slowPointer] = str(numOfReplica)
            slowPointer += 1
        else:
            numberOfSingleLetter += 1
    fastPointer = slowPointer - 1
    for i in range(numberOfSingleLetter):
        text.append(' ')
    slowPointer = len(text) - 1
    while fastPointer >= 0:
        if isNumber(text[fastPointer]):
            text[slowPointer] = text[fastPointer]
            fastPointer -= 1
            slowPointer -= 1
        else:
            text[slowPointer] = '1'
            slowPointer -= 1
        text[slowPointer] = text[fastPointer]
        slowPointer -= 1
        fastPointer -= 1
    return ''.join(text[slowPointer + 1 :])

testText7 = 'aaabbaacdd'
print(encodeString(testText7))

def findAnagram(text, segment):
    if len(text) == 0 or len(segment) == 0 or len(segment) > len(text):
        return
    hashTable = {}
    for index in range(len(segment)):
        if segment[index] not in hashTable:
            hashTable[segment[index]] = 1
        else:
            hashTable[segment[index]] += 1
    leftBound = 0
    rightBound = len(segment) - 1
    lettersLeft = len(hashTable)
    for index in range(len(segment)):
        if text[index] in hashTable:
            hashTable[text[index]] -= 1
            if hashTable[text[index]] == 0:
                lettersLeft -= 1
    if lettersLeft == 0:
        print(text[leftBound:rightBound + 1])
    leftBound += 1
    rightBound += 1
    while rightBound < len(text):
        if text[leftBound - 1] in hashTable:
            if hashTable[text[leftBound - 1]] == 0:
                lettersLeft += 1
            hashTable[text[leftBound - 1]] += 1
        if text[rightBound] in hashTable:
            hashTable[text[rightBound]] -= 1
            if hashTable[text[rightBound]] == 0:
                lettersLeft -= 1
        if lettersLeft == 0:
            print(text[leftBound:rightBound + 1])
        leftBound += 1
        rightBound += 1

testText8 = 'aabcbaa'
segment = 'aab'
findAnagram(testText8, segment)

