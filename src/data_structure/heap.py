class Heap(object):

    def __init__(self):
        self.array = []

    def _percolate_up_iteration(self, index):
        if index <= 0:
            return
        while index > 0:
            parent_index = (index - 1) // 2
            if self.array[index] < self.array[parent_index]:
                self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
                index = parent_index
            else:
                break

    def _percolate_up_recursion(self, index):
        if index <= 0:
            return
        parent_index = (index - 1) // 2
        if self.array[index] < self.array[parent_index]:
            self.array[parent_index], self.array[index] = self.array[index], self.array[parent_index]
            self._percolateUpRecursion(self, parent_index)

    def _percolate_down_iteration(self, index):
        if index > len(self.array) // 2 - 1:
            return
        while index <= len(self.array) // 2 - 1:
            index_left_child = index * 2 + 1
            index_right_child = index * 2 + 2
            index_min_child = index_left_child
            if index_right_child < len(self.array) and self.array[index_right_child] < self.array[index_left_child]:
                index_min_child = index_right_child
            if self.array[index] > self.array[index_min_child]:
                self.array[index], self.array[index_min_child] = self.array[index_min_child], self.array[index]
                index = index_min_child
            else:
                break

    def _percolate_down_recursion(self, index):
        if index > len(self.array) // 2 - 1:
            return
        index_left_child = index * 2 + 1
        index_right_child = index * 2 + 2
        index_min_child = index_left_child
        if index_right_child < len(self.array) and self.array[index_right_child] < self.array[index_left_child]:
            index_min_child = index_right_child
        if self.array[index] > self.array[index_min_child]:
            self.array[index], self.array[index_min_child] = self.array[index_min_child], self.array[index]
            self._percolateDownRecursion(self, index_min_child)

    def is_empty(self):
        return len(self.array) == 0

    def get_size(self):
        return len(self.array)

    def get_top(self):
        if len(self.array) > 0:
            return self.array[0]
        else:
            return None

    def pop(self):
        if self.is_empty():
            print('Heap is already empty!')
            return None
        result = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        if len(self.array) > 0:
            self._percolate_down_iteration(0)
        return result

    def insert(self, number):
        self.array.append(number)
        self._percolate_up_iteration(len(self.array) - 1)


def find_first_k_elements1(array, k):
    if not array or k >= len(array):
        return array
    h = Heap()
    for num in array:
        h.insert(num)
    result = []
    for i in range(k):
        result.append(h.pop())
    return result


def find_first_k_elements2(array, k):
    if not array or k >= len(array):
        return array
    h = Heap()
    for i in range(len(array)):
        if i < k:
            h.insert(-1 * array[i])
        elif h.get_top() < -1 * array[i]:
            h.pop()
            h.insert(-1 * array[i])
    result = []
    while not h.is_empty():
        result.append(-1 * h.pop())
    return result


def find_first_k_elements3(array, k, left_index, right_index):
    if not array or k >= right_index - left_index + 1 or k <= 0:
        return
    left = left_index
    right = right_index - 1
    while left <= right:
        if array[left] <= array[right_index]:
            left += 1
        else:
            array[left], array[right] = array[right], array[left]
            right -= 1
    array[left], array[right_index] = array[right_index], array[left]
    num_smaller = left - left_index
    if k == num_smaller or k == num_smaller + 1:
        return
    elif k < num_smaller:
        find_first_k_elements3(array, k, left_index, left - 1)
    else:
        find_first_k_elements3(array, k - num_smaller - 1, left + 1, right_index)


testHeap = Heap()
testArray = [2, 4, 2, 8, 5, 6, 1, 12, 9]
for element in testArray:
    testHeap.insert(element)
while not testHeap.is_empty():
    print(testHeap.pop(), end=' ')
print()

print(find_first_k_elements1(testArray, 3))
print(find_first_k_elements2(testArray, 3))
find_first_k_elements3(testArray, 7, 0, len(testArray) - 1)
print(testArray[:7])
