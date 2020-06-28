# class stack(object):
#     def __init__(self):
#         self.array = []
#         self.top = None
#
#     def push(self, value):
#         self.array.append(value)
#         self.top = self.array[-1]
#     def empty(self):
#         return self.array == []
#     def getlength(self):
#         return len(self.array)
#     def gettop(self):
#         return self.top
#     def pop(self):
#         if len(self.array) == 0:
#             return None
#         elif len(self.array) == 1:
#             result = self.array[-1]
#             self.array = []
#             self.top = None
#         else:
#             result = self.top
#             self.array = self.array[:-1]
#             self.top = self.array[-1]
#         return result

class stack(object):
    def __init__(self):
        self.array = []
        self.top = None
    def push(self, value):
        self.array.append(value)
        self.top = self.array[-1]
    def pop(self):
        if self.top == None:
            return None
        elif len(self.array) == 1:
            result = self.array[-1]
            self.top = None
            self.array = []
        else:
            result = self.array[-1]
            self.array = self.array[:-1]
            self.top = self.array[-1]
        return result
    def getlength(self):
        return len(self.array)
    def empty(self):
        return self.array == []
    def gettop(self):
        return self.top

def selection(sta):
    sorted = stack()
    sortednum = 0
    totallength = sta.getlength()
    while sortednum < totallength:
        mini = sta.gettop()
        repli = 0

        # find minimum and its replication
        while not sta.empty():
            tem = sta.pop()
            sorted.push(tem)
            if tem < mini:
                repli = 1
                mini = tem
            elif tem == mini:
                repli += 1

        # refill the sta with unsorted numbers
        for i in range(totallength - sortednum):
            tem = sorted.pop()
            if tem != mini:
                sta.push(tem)

        #push minimum in sorted stack repli times
        for i in range(repli):
            sorted.push(mini)

        # renew sortednum
        sortednum += repli
    return sorted


# def selection(s):
#     sorted = stack()
#     length = s.getlength()
#     count = 0
#     while count < length:
#         min = s.gettop()
#         repli = 0
#         while not s.empty():
#             tem = s.pop()
#             sorted.push(tem)
#             if tem < min:
#                 repli = 1
#                 min = tem
#             elif tem == min:
#                 repli += 1
#
#         for i in range(length - count):
#             tem = sorted.pop()
#             if tem != min:
#                 s.push(tem)
#
#         for i in range(repli):
#             sorted.push(min)
#         count += repli
#         # print([min, count])
#     return sorted

# class dequeue(object):
#     def __init__(self):
#         self.s1 = stack()
#         self.s2 = stack()
#         self.s3 = stack()
#     def push(self, value):
#         self.s2.push(value)
#     def pop1(self):
#         if self.s1.empty() and self.s2.empty():
#             return None
#         elif self.s1.empty():
#             len = self.s2.getlength() // 2
#             for i in range(len):
#                 tem = self.s2.pop()
#                 self.s3.push(tem)
#             while not self.s2.empty():
#                 tem = self.s2.pop()
#                 self.s1.push(tem)
#             while not self.s3.empty():
#                 tem = self.s3.pop()
#                 self.s2.push(tem)
#         return self.s1.pop()
#     def pop2(self):
#         if self.s1.empty() and self.s2.empty():
#             return None
#         elif self.s2.empty():
#             len = self.s1.getlength() // 2
#             for i in range(len):
#                 tem = self.s1.pop()
#                 self.s3.push(tem)
#             while not self.s1.empty():
#                 tem = self.s1.pop()
#                 self.s2.push(tem)
#             while not self.s3.empty():
#                 tem = self.s3.pop()
#                 self.s1.push(tem)
#         return self.s2.pop()
class dequeue(object):
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()
        self.s3 = stack()

    def push1(self,val):
        self.s1.push(val)

    def push2(self,val):
        self.s2.push(val)

    def pop1(self):
        if self.s1.empty() and self.s2.empty():
            return None
        elif self.s1.empty() and not self.s2.empty():
            len = self.s2.getlength()//2
            for i in range(len):
                tem = self.s2.pop()
                self.s3.push(tem)
            while not self.s2.empty():
                tem = self.s2.pop()
                self.s1.push(tem)
            while not self.s3.empty():
                tem = self.s3.pop()
                self.s2.push(tem)
            return self.s1.pop()
        else:
            return self.s1.pop()

    def pop2(self):
        if self.s1.empty() and self.s2.empty():
            return None
        elif self.s2.empty() and not self.s1.empty():
            len = self.s1.getlength()//2
            for i in range(len):
                tem = self.s1.pop()
                self.s3.push(tem)
            while not self.s1.empty():
                tem = self.s1.pop()
                self.s2.push(tem)
            while not self.s3.empty():
                tem = self.s3.pop()
                self.s1.push(tem)
            return self.s2.pop()
        else:
            return self.s2.pop()


class node(object):
    def __init__(self, val):
        self.value = val
        self.next = None

class linkedlist(object):
    def __init__(self):
        self.head = None

    def add(self, val):
        temnode = node(val)
        temnode.next = self.head
        self.head = temnode

    def show(self):
        cur = self.head
        while cur != None:
            print(cur.value, end = ' ')
            cur = cur.next
        print() # used to change the line

    def reverse(self):
        pre = None
        cur = self.head
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        self.head = pre

def reverse(head):
    if head == None or head.next == None:
        return head
    pre = None
    cur = head
    while cur != None:
        tem = cur.next
        cur.next = pre
        pre = cur
        cur = tem
    return pre

# def reverse1(head):
#     if head.next == None or head == None:
#          return head
#     subhead = reverse1(head.next)
#     head.next.next = head
#     head.next = None
#     return subhead
def reverse1(head):
    if head == None or head.next == None:
        return head
    newhead = reverse1(head.next)
    head.next.next = head
    head.next = None
    return newhead


# def midpoint(head):
#     if head == None:
#         return head
#     fast = slow = head
#     while fast.next != None and fast.next.next != None:
#         fast = fast.next.next
#         slow = slow.next
#     return slow.value

def midpoint(head):
    if head == None:
        return None
    slow = fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow.value

# def circle(head):
#     if head == None:
#         return  False
#     fast = slow = head
#     while fast.next != None and fast.next.next != None:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#     return False

def circle(head):
    if head == None:
        return False
    slow = fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

# head is a sorted linkedlist
def insert(head, node):
    if head == None:
        return node
    cur = head
    pre = None
    while cur != None and cur.value < node.value:
        pre = cur
        cur = cur.next

    if cur == head:
        node.next = cur
        return node
    elif cur == None:
        pre.next = node
        return head
    else:
        node.next = cur
        pre.next = node
        return head

test1 = [1, 5, 3, 5, 25, 2, 34, 9, 10]
test2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dq = dequeue()
st = stack()
for val in test1:
    dq.push1(val)
    st.push(val)
print(st.array)
print(dq.pop2())
snew = selection(st)
print(snew.array)

print('linklist test')

# 1 -> 2 ->3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
ll = linkedlist()
for val in test2:
    ll.add(val)
ll.show()

ll.reverse()
ll.show()

# ll.head = insert(ll.head, node(5))
# ll.show()

ll.head = reverse1(ll.head)
ll.show()

print(midpoint(ll.head))
print(circle(ll.head))

import DATAstructure
a = DATAstructure.Queue()

