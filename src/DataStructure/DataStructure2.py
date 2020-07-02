import DataStructure1 as DS1
print()

def selectionSort(array):
    if array == None or len(array) <= 1:
        return array
    stack = DS1.Stack()
    sorted = DS1.Stack()
    for element in array:
        stack.push(element)
    while stack.getSize() > 0:
        unsortedLength = stack.getSize()
        minimum = stack.getTop()
        replicaOfMinimum = 0
        while not stack.isEmpty():
            temporal = stack.pop()
            if temporal < minimum:
                minimum = temporal
                replicaOfMinimum = 1
            elif temporal == minimum:
                replicaOfMinimum += 1
            sorted.push(temporal)
        for i in range(unsortedLength):
            temporal = sorted.pop()
            if temporal != minimum:
                stack.push(temporal)
        for i in range(replicaOfMinimum):
            sorted.push(minimum)
    while not sorted.isEmpty():
        stack.push(sorted.pop())
    result = []
    while not stack.isEmpty():
        result.append(stack.pop())
    return result

testArray1 = [1, 5, 3, 5, 25, 2, 34, 9, 10]
print(selectionSort(testArray1))
# --------------------------------------------------------------------------------
class Deque(object):
    def __init__(self):
        self.stackLeft = DS1.Stack()
        self.stackRight = DS1.Stack()
        self.transfer = DS1.Stack()
    def pushLeft(self, element):
        self.stackLeft.push(element)
    def pushRight(self, element):
        self.stackRight.push(element)
    def popLeft(self):
        if self.stackLeft.getSize() == 0:
            if self.stackRight.getSize() == 0:
                print('Deque is empty!')
                return None
            else:
                for i in range(self.stackRight.getSize() // 2):
                    self.transfer.push(self.stackRight.pop())
                while not self.stackRight.isEmpty():
                    self.stackLeft.push(self.stackRight.pop())
                while not self.transfer.isEmpty():
                    self.stackRight.push(self.transfer.pop())
        return self.stackLeft.pop()
    def popRight(self):
        if self.stackRight.getSize() == 0:
            if self.stackLeft.getSize() == 0:
                print('Deque is empty!')
                return None
            else:
                for i in range(self.stackLeft.getSize() // 2):
                    self.transfer.push(self.stackLeft.pop())
                while not self.stackLeft.isEmpty():
                    self.stackRight.push(self.stackLeft.pop())
                while not self.transfer.isEmpty():
                    self.stackLeft.push(self.transfer.pop())
        return self.stackRight.pop()

deque = Deque()
for element in testArray1:
    deque.pushLeft(element)
print(deque.popRight())
# --------------------------------------------------------------------------------
class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedListIteration(head):
    if head == None or head.next == None:
        return head
    preNode = None
    curNode = head
    while curNode != None:
        nextNode = curNode.next
        curNode.next = preNode
        preNode = curNode
        curNode = nextNode
    return preNode

def reverseLinkedListRecursion(head):
    if head == None:
        return None
    # base case
    if head.next == None:
        return head
    nextNode = head.next
    newHead = reverseLinkedListRecursion(nextNode)
    nextNode.next = head
    head.next = None
    return newHead

def findMidPoint(head):
    if head == None or head.next == None:
        return head
    fastPointer = head
    slowPointer = head
    while fastPointer.next != None and fastPointer.next.next != None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    return slowPointer

def hasCircle(head):
    if head == None:
        return False
    slowPointer = fastPointer = head
    while fastPointer.next != None and fastPointer.next.next != None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if fastPointer == slowPointer:
            return True
    return False

def insertLinkedList(head, element):
    curNode = head
    preNode = None
    while curNode != None and curNode.value < element:
        preNode = curNode
        curNode = curNode.next
    if curNode == head:
        newHead = ListNode(element)
        newHead.next = curNode
        return newHead
    else:
        preNode.next = ListNode(element)
        preNode.next.next = curNode
        return head

def linkedListPrint(head):
    curNode = head
    while curNode != None:
        print(curNode.value, end=' ')
        curNode = curNode.next
    print()

testHead = ListNode(testArray1[0])
curNode = testHead
for index in range(1, len(testArray1)):
    curNode.next = ListNode(testArray1[index])
    curNode = curNode.next
# 1 -> 5 -> 3 -> 5 -> 25 -> 2 -> 34 -> 9 -> 10

print('LinkedList test:')
linkedListPrint(testHead)
reversedLinkedList = reverseLinkedListIteration(testHead)
linkedListPrint(reversedLinkedList)
linkedListPrint(reverseLinkedListRecursion(reversedLinkedList))

print(findMidPoint(testHead).value)

print(hasCircle(testHead))
curNode.next = testHead
print(hasCircle(testHead))

curNode.next = None
linkedListPrint(insertLinkedList(testHead, 0))

