# 1/7/2020
# def quicksort(array):
#     # stop point
#     if len(array) <= 1:
#         return array
#     # processing
#     i = 0
#     j = len(array) - 2
#     while i <= j:
#         if array[i] < array[-1]:
#             i += 1
#         else:
#             tem1 = array[i]
#             array[i] = array[j]
#             array[j] = tem1
#             j -= 1
#
#     # swap i and -1
#     tem2 = array[-1]
#     array[-1] = array[i]
#     array[i] = tem2
#
#     # merge
#     smaller = quicksort(array[:i])
#     larger = quicksort(array[i + 1:])
#     array = smaller + [array[i]] + larger
#     return array

# 1/9/2020
# def quicksort(array):
#     if len(array) <= 1:
#         return array
#     i = 0
#     j = len(array) - 2
#     while i <= j:
#         if array[i] < array[-1]:
#             i += 1
#         else:
#             tem1 = array[j]
#             array[j] = array[i]
#             array[i] = tem1
#             j -= 1
#     tem2 = array[i]
#     array[i] = array[-1]
#     array[-1] = tem2
#     left = quicksort(array[:i])
#     right = quicksort(array[i + 1:])
#     result = left + [array[i]] + right
#     return result

# 1/30/2020
# def quicksort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = array[-1]
#     i = 0
#     j = len(array) - 2
#     while i <= j:
#         if array[i] < pivot:
#             i += 1
#         else:
#             tem1 = array[i]
#             array[i] = array[j]
#             array[j] = tem1
#             j -= 1
#     tem2 = array[-1]
#     array[-1] = array[i]
#     array[i] = tem2
#     smaller = quicksort(array[:i])
#     bigger = quicksort(array[i + 1:])
#     result = smaller + [array[i]] + bigger
#     return result

# 3/9/2020
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    i = 0
    j = len(array) - 2
    while i <= j:
        if array[i] <= pivot:
            i += 1
        else:
            tem1 = array[j]
            array[j] = array[i]
            array[i] = tem1
            j -= 1
    tem2 = array[i]
    array[i] = array[-1]
    array[-1] = tem2
    smaller = quicksort(array[:i])
    bigger = quicksort(array[i + 1:])
    result = smaller + [array[i]] + bigger
    return result
def quicksort1(array):
    if len(array) <= 1:
        return array
    pivot = len(array) - 1
    i = 0
    j = pivot - 1
    while i <= j:
        if array[i] < array[pivot]:
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
            j -= 1
    array[i], array[pivot] = array[pivot], array[i]

    return quicksort1(array[:i]) + [array[i]] + quicksort1(array[i + 1:])
test = [1, 4, 6, 7, 3, 45, 8, 3, 7, 4, 8, 68, 23]
print(quicksort1(test))
# print(test[12:])