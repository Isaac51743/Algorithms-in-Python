import data_structure1 as ds1
import tree as t


print('simple Stack and Queue:')
stack1 = ds1.Stack()
queue1 = ds1.Queue()
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

print('queue of 2 stacks:')
queue2 = ds1.QueueOfTwoStack()
for num in range(10):
    queue2.push(num)
queue2.queue_print()
while not queue2.is_empty():
    print(queue2.pop(), end=' ')
print()

print('stack with min():')
testArray = [6, 6, 3, 6, 3, 3, 1, 2, 3]
stack2 = ds1.StackWithMin1()
for num in testArray:
    stack2.push(num)
stack2.stack_print()
while not stack2.is_empty():
    print(stack2.pop(), end=' ')
print()

stack3 = ds1.StackWithMin2()
for num in testArray:
    stack3.push(num)
stack3.stack_print()
while not stack3.is_empty():
    print(stack3.pop(), end=' ')
print()

print('Tree:')

t.pre_order(t.test_root1)
print()
t.in_order(t.test_root1)
print()
t.post_order(t.test_root1)
print()

print('tree height: ' + str(t.get_height(t.test_root1)))
print(t.is_balanced(t.test_root1))
print(t.is_symmetric(t.test_root2.left_child, t.test_root2.right_child))
print(t.is_identical(t.test_root1, t.test_root2))

print('whether a BST: ' + str(t.is_bst(t.test_root3, float('-inf'), float('inf'))))
t.in_order_in_range(t.test_root3, 9, 20)
print()

