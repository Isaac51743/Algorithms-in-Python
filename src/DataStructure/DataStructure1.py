class Stack(object):
    def __init__(self):
        self.array = []
    def push(self, element): # O(1)
        self.array.append(element)
    def pop(self): # amortized O(1)
        if len(self.array) == 0:
            print('Stack already empty!')
            return None
        topElement = self.array.pop()
        return topElement
    def getSize(self):
        return len(self.array)
    def getTop(self):
        if len(self.array) == 0:
            print('Stack already empty!')
            return None
        return self.array[-1]
    def isEmpty(self):
        return len(self.array) == 0
    def stackPrint(self, reverse = False): # the bottom is on the left in default
        if reverse:
            self.array.reverse()
            print(self.array)
            self.array.reverse()
        else:
            print(self.array)

class Queue(object):
    def __init__(self):
        self.array = []
    def isEmpty(self):
        return len(self.array) == 0
    def getSize(self):
        return len(self.array)
    def push(self, element):
        self.array.append(element)
    def pop(self):
        if len(self.array) == 0:
            return None
        result = self.array.pop(0)
        return result
    def queuePrint(self):
        print(self.array)

stack1 = Stack()
for element in range(10):
    stack1.push(element)
stack1.stackPrint()
while not stack1.isEmpty():
    print(stack1.pop(), end=' ')
print()
# ----------------------------------------------------------------------
class QueueOfTwoStack(object):
    def __init__(self):
        self.leftStack = Stack()
        self.rightStack = Stack()
    def push(self, element):
        self.leftStack.push(element)
    def pop(self):
        if self.rightStack.isEmpty():
            if self.leftStack.isEmpty():
                print('queue already empty')
                return None
            else:
                while not self.leftStack.isEmpty():
                    self.rightStack.push(self.leftStack.pop())
        return self.rightStack.pop()
    def queuePrint(self):
        self.leftStack.stackPrint(reverse = True)
        self.rightStack.stackPrint()
    def isEmpty(self):
        return self.leftStack.isEmpty() and self.rightStack.isEmpty()

queue1 = QueueOfTwoStack()
for element in range(10):
    queue1.push(element)
queue1.queuePrint()
while not queue1.isEmpty():
    print(queue1.pop(), end=' ')
print()
# ----------------------------------------------------------------------
class StackWithMin1():
    def __init__(self):
        self.stack = Stack()
        self.currentMin = Stack()
    def push(self, element):
        self.stack.push(element)
        if self.currentMin.isEmpty() or self.currentMin.getTop() > element:
            self.currentMin.push(element)
        else:
            self.currentMin.push(self.currentMin.getTop())
    def pop(self):
        self.currentMin.pop()
        return self.stack.pop()
    def getMin(self):
        return self.currentMin.getTop()
    def getSize(self):
        return self.stack.getSize()
    def getTop(self):
        return self.stack.getTop()
    def isEmpty(self):
        return self.stack.isEmpty()
    def stackPrint(self, reverse = False):
        self.stack.stackPrint(reverse)
        self.currentMin.stackPrint(reverse)

class StackWithMin2():
    def __init__(self):
        self.stack = Stack()
        # currentMin stores tuple having 2 elements,
        # first represents size, second represents the minimum value
        self.currentMin = Stack()
    def push(self, element):
        self.stack.push(element)
        if self.currentMin.isEmpty() or self.currentMin.getTop()[1] > element:
            self.currentMin.push((self.stack.getSize(), element))
    def pop(self):
        if self.currentMin.getSize() != 0 and self.currentMin.getTop()[0] == self.stack.getSize():
            self.currentMin.pop()
        return self.stack.pop()
    def getMin(self):
        if not self.currentMin.isEmpty():
            return self.currentMin.getTop()[1]
        else:
            return None
    def getSize(self):
        return self.stack.getSize()
    def getTop(self):
        return self.stack.getTop()
    def isEmpty(self):
        return self.stack.isEmpty()
    def stackPrint(self, reverse = False):
        self.stack.stackPrint(reverse)
        self.currentMin.stackPrint(reverse)

testArray = [6, 6, 3, 6, 3, 3, 1, 2, 3]

stack2 = StackWithMin1()
for element in testArray:
    stack2.push(element)
stack2.stackPrint()

stack3 = StackWithMin2()
for element in testArray:
    stack3.push(element)
stack3.stackPrint()
