

def selection_sort_with_2_stacks(array):
    if len(array) == 0:
        return None
    stack1 = [] # unsorted
    stack2 = [] # sorted
    for num in array:
        stack1.append(num)
    while len(stack1) > 0:
        minimum = float('inf')
        replica_num = 0
        unsorted_num = len(stack1)
        while len(stack1) > 0:
            temp = stack1.pop()
            if temp == minimum:
                replica_num += 1
            elif temp < minimum:
                minimum = temp
                replica_num = 1
            stack2.append(temp)
        for i in range(unsorted_num):
            temp = stack2.pop()
            if temp != minimum:
                stack1.append(temp)
        for i in range(replica_num):
            stack2.append(minimum)
    return stack2


test_array1 = [1, 5, 3, 5, 25, 2, 34, 9, 10]
print(selection_sort_with_2_stacks(test_array1))


class DequeWithThreeStack():

    def __init__(self):
        self.left_stack = []
        self.right_stack = []
        self.helper_stack = []

    def push_left(self, num):
        self.left_stack.append(num)

    def push_right(self, num):
        self.right_stack.append(num)

    def is_empty(self):
        return len(self.left_stack) == 0 and len(self.right_stack) == 0

    def pop_left(self):
        if self.is_empty():
            return None
        elif len(self.left_stack) == 0:
            shift_num = len(self.right_stack) // 2
            for i in range(shift_num):
                self.helper_stack.append(self.right_stack.pop())
            while len(self.right_stack) > 0:
                self.left_stack.append(self.right_stack.pop())
            while len(self.helper_stack) > 0:
                self.right_stack.append(self.helper_stack.pop())
        return self.left_stack.pop()

    def pop_right(self):
        if self.is_empty():
            return None
        elif len(self.right_stack) == 0:
            shift_num = len(self.left_stack) // 2
            for i in range(shift_num):
                self.helper_stack.append(self.left_stack.pop())
            while len(self.left_stack) > 0:
                self.right_stack.append(self.left_stack.pop())
            while len(self.helper_stack) > 0:
                self.left_stack.append(self.helper_stack.pop())
        return self.right_stack.pop()


deque = DequeWithThreeStack()
for element in test_array1:
    deque.push_left(element)
print(deque.pop_right())


class ListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list_iteration(head):
    if not head:
        return head
    pre_node = None
    cur_node = head
    while cur_node:
        next_node = cur_node.next
        cur_node.next = pre_node
        pre_node = cur_node
        cur_node = next_node
    return pre_node


def reverse_linked_list_recursion(head):
    if not head or not head.next:
        return head
    new_head = reverse_linked_list_recursion(head.next)
    head.next.next = head
    head.next = None
    return new_head


def find_mid_point(head):
    if not head:
        return head
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def has_circle(head):
    if not head:
        return False
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def insert_linked_list(head, num):
    cur = head
    pre = None
    while cur and cur.value < num:
        pre = cur
        cur = cur.next
    if cur == head:
        new_head = ListNode(num)
        new_head.next = head
        return new_head
    else:
        pre.next = ListNode(num)
        pre.next.next = cur
        return head


def linked_list_print(head):
    cur = head
    while cur:
        print(cur.value, end=' ')
        cur = cur.next
    print()


test_head = ListNode(test_array1[0])
curNode = test_head
for index in range(1, len(test_array1)):
    curNode.next = ListNode(test_array1[index])
    curNode = curNode.next
# 1 -> 5 -> 3 -> 5 -> 25 -> 2 -> 34 -> 9 -> 10

print('LinkedList test:')
linked_list_print(test_head)
reversed_head = reverse_linked_list_iteration(test_head)
linked_list_print(reversed_head)
linked_list_print(reverse_linked_list_recursion(reversed_head))

print(find_mid_point(test_head).value)

print(has_circle(test_head))
reversed_head.next = test_head
print(has_circle(test_head))
reversed_head.next = None

linked_list_print(insert_linked_list(test_head, 0))

