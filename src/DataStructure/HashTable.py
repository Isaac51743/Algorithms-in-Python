class heap(object):
    def __init__(self):
        self.array = []

    def percolateup(self,index):
        if index <= 0:
            return None
        parent = (index - 1) // 2
        if self.array[index][0] < self.array[parent][0]:
            tem = self.array[index]
            self.array[index] = self.array[parent]
            self.array[parent] = tem
            self.percolateup(parent)

    def percolatedown(self, index):
        left = index * 2 + 1
        right = left + 1
        if right <= len(self.array) - 1:
            if self.array[left][0] < self.array[right][0]:
                min = left
            else:
                min = right
            if self.array[index][0] > self.array[min][0]:
                tem = self.array[index]
                self.array[index] = self.array[min]
                self.array[min] = tem
                self.percolatedown(min)
        elif left <= len(self.array) - 1:
            if self.array[left][0] < self.array[index][0]:
                tem = self.array[left]
                self.array[left] = self.array[index]
                self.array[index] = tem
                self.percolatedown(left)

    def insert(self, val):
        self.array.append(val)
        self.percolateup(len(self.array) - 1)
        return self.array

    def update(self, index, val):
        if val[0] == self.array[index][0]:
            return self.array

        if val[0] > self.array[index][0]:
            self.array[index] = val
            self.percolatedown(index)
        elif val[0] < self.array[index][0]:
            self.array[index] = val
            self.percolateup(index)
        return self.array

    def pop(self):
        if len(self.array) == 0:
            return None
        if len(self.array) == 1:
            tem = self.array[0]
            self.array = []
            return tem
        result = self.array[0]
        self.array[0] = self.array[-1]
        self.array = self.array[:-1]
        self.percolatedown(0)
        return result

    def empty(self):
        return self.array == []

def kfrequent(st, k):
    dic = {}
    st = st.replace(',', '')
    st = st.replace('.', '')
    st = st.replace('?', '')
    words = st.split(' ')
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    print(dic)
    pq = heap()
    for key in dic:
        pq.insert([-1 * dic[key], key])
    for i in range(k):
        result = pq.pop()
        result = [-1 * result[0]] + result[1:]
        print(result)
def missingnum(array):
    dic = {}
    for i in array:
        dic[i] = 1
    for i in range(min(array), max(array) + 1):
        if i not in dic:
            print(i)
def missingnum1(array):
    XOR = 0
    for item in array:
        XOR = XOR ^ item
    for i in range(min(array), max(array) + 1):
        XOR = XOR ^ i
    print(XOR)
def common(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return None
    dic = {}
    result = []
    if len(a1) < len(a2):
        for item in a1:
            dic[item] = 1
        for item in a2:
            if item in dic:
                result.append(item)
    else:
        for item in a2:
            dic[item] = 1
        for item in a1:
            if item in dic:
                result.append(item)
    return result
def common1(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return None
    i = j = 0
    result = []
    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            result.append(a1[i])
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            j += 1
    return result
test = 'i love you so much, but you do not love me. can you hug me a little bit?'
kfrequent(test, 3)
test1 = [3, 2, 7, 4, 10, 6, 9, 8]
test2 = [11, 6, 14, 8, 3, 2, 12, 4]
missingnum1(test1)
print(common(test1, test2))
test3 = [1, 3, 5, 7, 8, 12, 24]
test4 = [1, 3, 6, 7, 10, 12, 14]
print(common1(test3, test4))