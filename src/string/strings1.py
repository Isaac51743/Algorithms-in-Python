def char_removal1(text, char_set):
    if len(text) == 0:
        return ''
    text_list = list(text)
    slow = 0
    for fast in range(len(text_list)):
        if text_list[fast] not in char_set:
            text_list[slow], text_list[fast] = text_list[fast], text_list[slow]
            slow += 1
    return ''.join(text_list[:slow])


# unordered, method like quick sort
# this method is used to divided the list into two parts.
def char_removal2(text, char_set):
    if len(text) == 0:
        return ''
    text_list = list(text)
    left = 0
    right = len(text_list) - 1
    while left <= right:
        if text_list[left] not in char_set:
            left += 1
        else:
            text_list[left], text_list[right] = text_list[right], text_list[left]
            right -= 1
    return ''.join(text_list[:left])

def spaceRemoval(text):
    if len(text) == 0:
        return None
    text = list(text)
    slowPointer = fastPointer = 0
    wordsNum = 0
    while True:
        while fastPointer < len(text) and text[fastPointer] == ' ':
            fastPointer += 1
        if fastPointer == len(text):
            break
        if wordsNum > 0:
            text[slowPointer] = ' '
            slowPointer += 1
        while fastPointer < len(text) and text[fastPointer] != ' ':
            text[slowPointer], text[fastPointer] = text[fastPointer], text[slowPointer]
            slowPointer += 1
            fastPointer += 1
        wordsNum += 1
    return ''.join(text[:slowPointer])


testText1 = '   zhaoyuehang is a     handsome man  '
print(char_removal1(testText1, {'a', 'o'}))
print(char_removal2(testText1, {'a', 'o'}))
print(spaceRemoval(testText1))


def deduplication(text):
    if len(text) <= 1:
        return text
    text = list(text)
    slowPointer = 1
    for fastPointer in range(1, len(text)):
        if text[fastPointer] != text[slowPointer - 1]:
            text[fastPointer], text[slowPointer] = text[slowPointer], text[fastPointer]
            slowPointer += 1
    return ''.join(text[:slowPointer])


def deleteContiguousSameLetter(text):
    if len(text) <= 1:
        return text
    text = list(text)
    stackTop = -1
    index = 0
    while index < len(text):
        if stackTop < 0 or text[stackTop] != text[index]:
            stackTop += 1
            text[stackTop], text[index] = text[index], text[stackTop]
            index += 1
        else:
            while index < len(text) and text[index] == text[stackTop]:
                index += 1
            stackTop -= 1
    return ''.join(text[:stackTop + 1])


testText2 = 'thissss messsege     hasss nnno dduppllicatttion'
print(deduplication(testText2))
testText3 = 'zbbccccbbyeeeehee'
print(deleteContiguousSameLetter(testText3))


def orderOfLetter(letter):
    return ord(letter) - ord('a') + 1


# assuming lower case letter
def findSubString(text, segment):
    if len(text) == 0 or len(segment) == 0 or len(segment) > len(text):
        return None
    text = list(text)
    segment = list(segment)
    segmentHashValue = 0
    textHashValue = 0
    for index in range(len(segment)):
        textHashValue = textHashValue + 26 ** index * orderOfLetter(text[index])
        segmentHashValue = segmentHashValue + 26 ** index * orderOfLetter(segment[index])
    startIndex = 0
    endIndex = len(segment) - 1
    position = []
    while endIndex < len(text):
        if startIndex > 0:
            textHashValue = (textHashValue - orderOfLetter(text[startIndex - 1])) // 26 + orderOfLetter(text[endIndex]) * 26 ** (len(segment) - 1)
        if textHashValue == segmentHashValue:
            position.append(startIndex)
        startIndex += 1
        endIndex += 1
    return position


testText4 = 'hzabcbchooifahabcbcfoinabcbce'
segment = 'abcbc'
print(findSubString(testText4, segment))


