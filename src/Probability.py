import random as R
import Heap as H
print('Probability:')

def shufflePoker(array):
    if len(array) != 52:
        print('invalid array')
        return
    for index in range(len(array)):
        randomIndex = R.randint(index, len(array) - 1)
        array[index], array[randomIndex] = array[randomIndex], array[index]
testArray = [i for i in range(52)]
shufflePoker(testArray)
print(testArray)
# -----------------------------------------------------------------------------------
def getRandomElementInFlow(input, timeIndex):
    if R.randint(0, timeIndex) == 0:
        global randomElement
        randomElement = input

def getRandomKElementInFlow(input, timeIndex, k):
    randomIndex = R.randint(0, timeIndex)
    if randomIndex < k:
        global randomKElement
        randomKElement[randomIndex] = input

testFlow1 = [1, 3, 9, 5, 2, 7, 12, 21, 8, 6]
randomElement = None
for index, value in enumerate(testFlow1):
    getRandomElementInFlow(value, index)
    print(randomElement, end=' ')
print()

k = 3
randomKElement = testFlow1[:k]
for index in range(k, len(testFlow1)):
    getRandomKElementInFlow(testFlow1[index], index, k)
    print(randomKElement, end=' ')
print()
# -----------------------------------------------------------------------------------
indexOfLargestElement = []
largestElement = None
def getRandomIndexOfLargestElement(input, timeIndex):
    global indexOfLargestElement, largestElement, randomIndexOfLargestElement
    if largestElement == None:
        indexOfLargestElement.append(timeIndex)
        largestElement = input
    elif input == largestElement:
        indexOfLargestElement.append(timeIndex)
    elif input > largestElement:
        indexOfLargestElement = [timeIndex]
        largestElement = input
    randomIndexOfLargestElement = indexOfLargestElement[R.randint(0, len(indexOfLargestElement) - 1)]

randomIndexOfLargestElement = -1
testFlow2 = [1, 3, 9, 5, 2, 3, 9, 2, 9, 2]
for index, value in enumerate(testFlow2):
    getRandomIndexOfLargestElement(value, index)
    print(randomIndexOfLargestElement, end=' ')
print()
# -----------------------------------------------------------------------------------
def generatorWithSize5():
    randomNumber = R.randint(0, 7)
    while randomNumber > 4:
        randomNumber = R.randint(0, 7)
    return randomNumber

def generatorWithSize7():
    row = R.randint(0, 5)
    column = R.randint(0, 5)
    while row * 5 + column >= (4 * 5 + 4) // 7 * 7:
        row = R.randint(0, 5)
        column = R.randint(0, 5)
    return (row * 5 + column) % 7

for i in range(10):
    print(generatorWithSize5(), end=' ')
print()
for i in range(10):
    print(generatorWithSize7(), end=' ')
print()
# -----------------------------------------------------------------------------------
smallerHeap = H.Heap()
biggerHeap = H.Heap()
def getMedianOfFlow(input):
    if smallerHeap.getSize() == 0:
        smallerHeap.insert(-1 * input)
    elif smallerHeap.getSize() > biggerHeap.getSize():
        if input > -1 * smallerHeap.getTop():
            biggerHeap.insert(input)
        else:
            smallerHeap.insert(-1 * input)
            biggerHeap.insert(-1 * smallerHeap.pop())
    elif smallerHeap.getSize() == biggerHeap.getSize():
        if input > -1 * smallerHeap.getTop():
            biggerHeap.insert(input)
            smallerHeap.insert(-1 * biggerHeap.pop())
        else:
            smallerHeap.insert(-1 * input)
    if smallerHeap.getSize() == biggerHeap.getSize():
        return (-1 * smallerHeap.getTop() + biggerHeap.getTop()) / 2
    else:
        return -1 * smallerHeap.getTop()

for element in testFlow2:
    print(getMedianOfFlow(element), end=' ')
print()