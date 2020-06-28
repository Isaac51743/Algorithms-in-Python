# 1/6/2020
# def recursion(array, left, right):
#     if left == right:
#         return [array[left]]
#     mid = left + (right - left) // 2
#     leftarray = recursion(array, left, mid)
#     rightarray = recursion(array, mid + 1, right)
#     finalarray = merge(leftarray, rightarray)
#     return finalarray

# def merge(array1, array2):
#     finalarray = []
#     i = j = 0
#     while len(finalarray) < (len(array1) + len(array2)):
#         if i < len(array1) and j < len(array2):
#             if array1[i] < array2[j]:
#                 finalarray.append(array1[i])
#                 i += 1
#             else:
#                 finalarray.append(array2[j])
#                 j += 1
#         elif i >= len(array1) and j < len(array2):
#             finalarray.extend(array2[j:])
#         else:
#             finalarray.extend(array1[i:])
#     return finalarray

# 1/9/2020
# def divide(array):
#     if len(array) <= 1:
#         return array
#     mid = (len(array) - 1)//2
#     leftpart = divide(array[:mid + 1])
#     rightpart = divide(array[mid + 1:])
#     result = merge(leftpart, rightpart)
#     return result
# def merge(left, right):
#     i = j = 0
#     result = []
#     while len(result) < len(left) + len(right):
#         if i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#         elif i >= len(left):
#             result.extend(right[j:])
#         else:
#             result.extend(left[i:])
#     return result

# reverse merge
# array must be 4^n
def reverse(array, left, right):
    if (right - left + 1) < 4:
        return array[left:right + 1]
    cut1 = left + (right - left + 1)//4
    cut2 = left + 2 * ((right - left + 1)//4)
    cut3 = left + 3 * ((right - left + 1)//4)
    # print([cut1, cut2, cut3])
    array = array[:cut1] + array[cut2:cut3] + array[cut1:cut2] + array[cut3:]
    leftpart = reverse(array, left, cut2 - 1)
    rightpart = reverse(array, cut2, right)
    final = leftpart + rightpart
    return final

# 1/28/2020
# def mergesort(array, left, right):
#     if left == right:
#         return [array[left]]
#     mid = left + (right - left) //2
#     leftsorted = mergesort(array, left, mid)
#     rightsorted = mergesort(array, mid + 1, right)
#     result = merge(leftsorted, rightsorted)
#     return result
# def merge(a, b):
#     i = j = 0
#     result = []
#     while len(result) < len(a) + len(b):
#         if i < len(a) and j < len(b):
#             if a[i] < b[j]:
#                 result.append(a[i])
#                 i += 1
#             else:
#                 result.append(b[j])
#                 j += 1
#         elif i >= len(a):
#             result.extend(b[j:])
#         else:
#             result.extend(a[i:])
#     return result
def mergesort(array, left, right):
    if left == right:
        return [array[left]]
    mid = left + (right - left)//2
    leftsorted = mergesort(array, left, mid)
    rightsorted = mergesort(array, mid + 1, right)
    result = merge(leftsorted, rightsorted)
    return result
def merge(left, right):
    i = j = 0
    result = []
    while i <= len(left) - 1 or j <= len(right) - 1:
        if i <= len(left) - 1 and j <= len(right) - 1:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i > len(left) - 1:
            result.extend(right[j:])
            j = len(right)
        else:
            result.extend(left[i:])
            i = len(left)
    return result

test1 = [1, 2, 4, 5, 3, 5, 7, 2, 0, 9, 6]
test2 = [1, 2, 3, 4, 5, 6, 7, 8]
result1 = mergesort(test1, 0, len(test1) - 1)
result2 = reverse(test2, 0, len(test2) - 1)
print(result1)