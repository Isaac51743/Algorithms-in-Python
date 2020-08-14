# 08/14/2020


class Stack(object):

    def __init__(self):
        self.array = []

    def push(self, element):  # O(1)
        self.array.append(element)

    def pop(self):  # O(1)
        if len(self.array) == 0:
            print('Stack already empty!')
            return None
        return self.array.pop()

    def get_size(self):
        return len(self.array)

    def get_top(self):
        if len(self.array) == 0:
            print('Stack already empty!')
            return None
        return self.array[-1]

    def is_empty(self):
        return len(self.array) == 0

    def stack_print(self, reverse=False):  # the bottom is on the left in default
        if reverse:
            self.array.reverse()
            print(self.array)
            self.array.reverse()
        else:
            print(self.array)


class Queue(object):

    def __init__(self):
        self.array = []

    def is_empty(self):
        return len(self.array) == 0

    def get_size(self):
        return len(self.array)

    def push(self, element):
        self.array.append(element)

    def pop(self):
        if len(self.array) == 0:
            return None
        return self.array.pop(0)

    def queue_print(self):
        print(self.array)


stack1 = Stack()
queue1 = Queue()
for num in range(10):
    stack1.push(num)
    queue1.push(num)
stack1.stack_print()
queue1.queue_print()
while not stack1.is_empty():
    print(stack1.pop(), end=' ')
print()
while not queue1.is_empty():
    print(queue1.pop(), end=' ')
print()


class QueueOfTwoStack(object):

    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def push(self, element):
        self.right_stack.append(element)

    def pop(self):
        if len(self.left_stack) == 0 and len(self.right_stack) == 0:
            return None
        elif len(self.left_stack) == 0:
            while len(self.right_stack) > 0:
                self.left_stack.append(self.right_stack.pop())
            return self.left_stack.pop()
        else:
            return self.left_stack.pop()

    def queue_print(self):
        self.left_stack.reverse()
        print(self.left_stack, end=' ')
        self.right_stack.reverse()
        print(self.right_stack)

    def is_empty(self):
        return len(self.left_stack) == 0 and len(self.right_stack) == 0


queue2 = QueueOfTwoStack()
for num in range(10):
    queue2.push(num)
queue2.queue_print()
while not queue2.is_empty():
    print(queue2.pop(), end=' ')
print()


class StackWithMin1():

    def __init__(self):
        self.stack = []
        self.cur_min = []

    def push(self, element):
        self.stack.append(element)
        if len(self.cur_min) == 0 or element < self.cur_min[-1]:
            self.cur_min.append(element)
        else:
            self.cur_min.append(self.cur_min[-1])

    def pop(self):
        self.cur_min.pop()
        return self.stack.pop()

    def get_min(self):
        return self.cur_min[-1] if len(self.cur_min) > 0 else None

    def get_size(self):
        return len(self.stack)

    def get_top(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    def is_empty(self):
        return len(self.stack) == 0

    def stack_print(self):
        print(self.stack)
        print(self.cur_min)


class StackWithMin2():

    def __init__(self):
        self.stack = []
        # current_min stores tuples with 2 elements
        # first represents size, second represents the minimum value
        self.cur_min = []

    def push(self, element):
        self.stack.append(element)
        if len(self.cur_min) == 0 or element < self.cur_min[-1][-1]:
            self.cur_min.append((len(self.stack), element))

    def pop(self):
        if len(self.cur_min) > 0 and len(self.stack) == self.cur_min[-1][0]:
            self.cur_min.pop()
        return self.stack.pop()

    def get_min(self):
        return self.cur_min[-1][-1] if len(self.cur_min) > 0 else None

    def get_size(self):
        return len(self.stack)

    def get_top(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    def is_empty(self):
        return len(self.stack) == 0

    def stack_print(self):
        print(self.stack)
        print(self.cur_min)


testArray = [6, 6, 3, 6, 3, 3, 1, 2, 3]

stack2 = StackWithMin1()
for num in testArray:
    stack2.push(num)
stack2.stack_print()
while not stack2.is_empty():
    print(stack2.pop(), end=' ')
print()

stack3 = StackWithMin2()
for num in testArray:
    stack3.push(num)
stack3.stack_print()
while not stack3.is_empty():
    print(stack3.pop(), end=' ')
print()
