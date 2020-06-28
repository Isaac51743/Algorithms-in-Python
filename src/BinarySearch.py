# 1/9/2020
# def search(array, left, right, target):
#     if left > right:
#         return -1
#     mid = left + (right - left) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         right = mid - 1
#         result = search(array, left, right, target)
#     else:
#         left = mid + 1
#         result = search(array, left, right, target)
#     return result

# def search2(array, target):
#     # first judge empty matrix
#     if len(array) == 0:
#         return -1
#     left =  0
#     right = len(test) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if target == array[mid]:
#             return mid
#         elif target > array[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# 1/11/2020
# def search(array, target):
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         mid = left + (right - left)//2
#         if target > array[mid]:
#             left = mid + 1
#         elif target < array[mid]:
#             right = mid - 1
#         else:
#             return mid
#     return -1

# def search2(array, left, right, target):
#     if left > right:
#         return -1
#     mid = left + (right - left)//2
#     if target == array[mid]:
#         return mid
#     elif target > array[mid]:
#         left = mid + 1
#         result = search2(array, left, right, target)
#     else:
#         right = mid - 1
#         result = search2(array, left, right, target)
#     return result
# 3/10/2020
def search(array, left, right, target):
    if left > right:
        return -1
    mid = left + (right - left)//2
    if array[mid] > target:
        right = mid - 1
    elif array[mid] == target:
        return mid
    else:
        left = mid + 1
    result = search(array, left, right, target)
    return result
# 1/12/2020
# def search2D(array, target):
#     row = len(array)
#     column = len(array[0])
#     left = 0
#     right = row * column - 1
#     while left <= right:
#         mid = left + (right - left)//2
#         if target > array[mid // column][mid % column]:
#             left = mid + 1
#         elif target < array[mid // column][mid % column]:
#             right = mid - 1
#         else:
#             return [mid // column, mid % column]
#     return -1

# def searchclosest(array, target):
#     left = 0
#     right = len(array) - 1
#     if len(array) < 1:
#         return -1
#     while left < right - 1:
#         mid = left + (right - left)//2
#         if target > array[mid]:
#             left = mid
#         elif target < array[mid]:
#             right = mid
#         else:
#             return mid
#     # post processing
#     if abs(left - target) > abs(right - target):
#         return array[right]
#     else:
#         return array[left]
# def firstoccur(array, target):
#     left = 0
#     right = len(array) - 1
#     while left < right - 1:
#         mid = left + (right - left)//2
#         if target > array[mid]:
#             left = mid + 1
#         elif target < array[mid]:
#             right = mid - 1
#         else:
#             right = mid
#     if array[left] == target:
#         return left
#     elif array[right] == target:
#         return right
#     else:
#         return -1
# def unknown(dic, target):
#     left = 0
#     right = 1
#     while dic.get(right) and dic.get(right) < target:
#         left = right + 1
#         right = right * 2
#     while left <= right:
#         mid = left + (right - left)//2
#         if dic.get(mid):
#             if target < dic.get(mid):
#                 right = mid - 1
#             elif target > dic.get(mid):
#                 left = mid + 1
#             else:
#                 return mid
#         right = mid - 1
#     return -1


# 1/13/2020
# def search(array, left, right, target):
#     if left > right:
#         return -1
#     mid = left + (right - left)//2
#     if target == array[mid]:
#         return mid
#     elif target > array[mid]:
#         left = mid + 1
#         result = search(array, left, right, target)
#     else:
#         right = mid - 1
#         result = search(array, left, right, target)
#     return result
def search2D(array, left, right, target, columns):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    row = mid // columns
    column = mid % columns
    if target == array[row][column]:
        return [row, column]
    elif target > array[row][column]:
        left = mid + 1
        result = search2D(array, left, right, target, columns)
    else:
        right = mid - 1
        result = search2D(array, left, right, target, columns)
    return result
# def closest(array, target):
#     left = 0
#     right = len(array) - 1
#     index = 0
#     while left <= right:
#         mid = left + (right - left) // 2
#         if abs(target - array[index]) > abs(target - array[mid]):
#             index = mid
#
#         if target == array[mid]:
#             return mid
#         elif target > array[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return index

# def first( array, target):
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if target == array[mid]:
#             if mid == 0 or array[mid - 1] < target:
#                 return mid
#             else:
#                 right = mid - 1
#         elif target > array[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# 1/30/2020
# def search(array, left, right, target):
#     if left > right:
#         return None
#     mid = left + (right - left) // 2
#     if target == array[mid]:
#         return mid
#     elif target > array[mid]:
#         left = mid + 1
#         result = search(array, left, right, target)
#     else:
#         right = mid - 1
#         result = search(array, left, right, target)
#     return result
def searchloop(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left)//2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return None
# def closet(array, target):
#     left = 0
#     right = len(array) - 1
#     while left < right - 1:
#         mid = left + (right - left)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             right = mid
#         else:
#             left = mid
#     if abs(array[left] - target) > abs(array[right] - target):
#         return right
#     else:
#         return left
# def first(array, target):
#     if len(array) == 0:
#         return None
#     left = 0
#     right = len(array) - 1
#     while left < right - 1:
#         mid = left + (right - left)//2
#         if array[mid] == target:
#             right = mid
#         elif array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     if array[left] == target:
#         return left
#     elif array[right] == target:
#         return right
#     else:
#         return None

# 3/11/2020
def first(array, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left)//2
    if array[mid] == target:
        if mid == 0 or array[mid - 1] != target:
            return mid
        else:
            right = mid - 1
            result = first(array, target, left, right)
    elif array[mid] < target:
        left = mid + 1
        result = first(array, target, left, right)
    else:
        right = mid - 1
        result = first(array, target, left, right)
    return result
def closet(array, target):
    if len(array) <= 1:
        return array
    left = 0
    right = len(array) - 1
    while left < right - 1:
        mid = left + (right - left)//2
        if array[mid] > target:
            right = mid
        elif array[mid] < target:
            left = mid
        else:
            return mid
    if abs(array[right] - target) < abs(array[left] - target):
        return right
    else:
        return left
def getsize(array):
    if array == None or array == []:
        return 0
    number = 1
    while number <= len(array):
        number = number * 2
    # binary search for idx//2 to idx
    start = number//2
    end = number - 1
    while start <= end:
        mid = start + (end - start)//2
        if mid == len(array):
            return mid
        elif mid < len(array):
            start = mid + 1
        else:
            end = mid - 1

def largestSmallerEqual(array, target):
    if array == None or len(array) == 0:
        return None
    left = 0
    right = len(array) - 1
    while left < right - 1:
        print(array[left:right + 1])
        mid = left + (right - left) // 2
        if array[mid] < target:
            left = mid
        elif target < array[mid]:
            right = mid
        else:
            left = mid
    print(array[left:right + 1])
    if array[right] <= target:
        return right
    else:
        return left
test = [[1, 4, 6], [8, 9, 12], [24, 35, 67]]
test2 =[2, 4, 6, 8, 9, 14, 14, 16, 17, 25, 27, 34, 56]
dic = {1: 2, 2: 4, 3: 5, 4  : 8, 5: 10, 6: 19}
bsearch = search(test2, 0, len(test2) - 1, 6)
final = first(test2, 14, 0, len(test2) - 1)
clo = closet(test2, 10)
print(clo)
print(getsize(test2))
print(largestSmallerEqual(test2, 14))