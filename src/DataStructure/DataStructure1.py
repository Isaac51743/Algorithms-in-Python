class Queue(object):
    def __init__(self):
        self.array = []
    def push(self, item):
        self.array.append(item)
    def pop(self):
        if len(self.array) == 0:
            return None
        tem = self.array[0]
        self.array = self.array[1:]
        return tem

class Stack(object):
    def __init__(self):
        self.array = []
        self.top = None
    def push(self, item):
        self.array.append(item)
        self.top = len(self.array) - 1
    def empty(self):
        return self.array == []
    def gettop(self):
        if len(self.array) == 0:
            return None
        else:
            return self.array[self.top]
    def pop(self):
        if len(self.array) == 0:
            return None
        elif len(self.array) == 1:
            tem = self.array[self.top]
            self.top = None
            self.array = self.array[:-1]
            return tem
        else:
            tem = self.array[self.top]
            self.top = len(self.array) - 2
            self.array = self.array[:-1]
            return tem

# 1/30/2020
class stack(object):
    def __init__(self):
        self.array = []
        self.top = None
    def push(self, value):
        self.array.append(value)
        self.top = self.array[-1]
    def empty(self):
        return self.array == []
    def gettop(self):
        return self.top
    def pop(self):
        if len(self.array) == 0:
            return None
        elif len(self.array) == 1:
            result = self.array[-1]
            self.array = []
            self.top = None
        else:
            result = self.top
            self.array = self.array[:-1]
            self.top = self.array[-1]
        return result

# test = stack()
# for i in range(10):
#     test.push(i)
# print(test.array)
# while not test.empty():
#     print(test.pop())

class Queue1(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, item):
        self.stack1.push(item)

    def pop(self):
        if self.stack1.empty() and self.stack2.empty():
            return None
        elif not self.stack1.empty() and self.stack2.empty():
            while not self.stack1.empty():
                tem1 = self.stack1.pop()
                self.stack2.push(tem1)
            tem2 = self.stack2.pop()
            return tem2
        else:
            tem = self.stack2.pop()
            return tem

class Stack_min(object):
    def __init__(self):
        self.stack = Stack()
        self.record = Stack()
        self.top = self.stack.top

    def push(self, item):
        self.stack.push(item)
        if self.record.empty() or item < self.record.gettop():
            self.record.push(item)
        else:
            self.record.push(self.record.gettop())

    def min(self):
        return self.record.gettop()

    def pop(self):
        tem = self.stack.pop()
        self.record.pop()
        return tem

# 2/2/2020
class Stack_minAdvance(object):
    def __init__(self):
        self.stack = Stack()
        self.record = Stack()
        self.top = self.stack.top

    def push(self, item):
        self.stack.push(item)
        # must see whether record is empty (can not see stack)
        if self.record.empty() or item < self.record.gettop()[0]:
            self.record.push([item, self.stack.top])

    def pop(self):
        if self.record.empty():
            return None

        if self.record.gettop()[-1] == self.stack.top:
            self.record.pop()
        tem = self.stack.pop()
        return tem

    def min(self):
        if self.record.empty():
            return None
        else:
            return self.record.gettop()[0]


test = Stack_minAdvance()
a = [6, 6, 3, 6, 3, 3, 1, 2, 3]
for i in a:
    test.push(i)
print(test.record.array)
print(test.stack.array)
for i in range(len(a)):
    m = test.min()
    t = test.pop()
    print([m, t])
