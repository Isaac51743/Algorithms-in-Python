# 12/27/2019
# def selection (a) :
#     for i in range(len(a) - 1) :
#         idx = i
#         for j in range(i+1, len(a)) :
#             if a[j] < a[idx] :
#                 idx = j
#         tem = a[idx]
#         a[idx] = a[i]
#         a[i] = tem
#     return a

# # 1/6/2020
# def selection(array):
#     for i in range(0, len(array) - 1):
#         idx = i
#         for j in range(i, len(array)):
#             if array[j] < array[idx]:
#                 idx = j
#         tem = array[idx]
#         array[idx] = array[i]
#         array[i] = tem
#     return array

# 1/9/2020
# def selection(array):
#     for i in range(0, len(array) - 1):
#         idx = i
#         for j in range(i, len(array)):
#             if array[j] < array[idx]:
#                 idx = j
#         tem = array[idx]
#         array[idx] = array[i]
#         array[i] = tem
#     return array

# 1/28/2020
# def selection(array):
#     for i in range(len(array) - 1) :
#         idx = i
#         for j in range(i + 1, len(array)) :
#             if array[idx] > array[j]:
#                 idx = j
#         tem = array[idx]
#         array[idx] = array[i]
#         array[i] = tem
#     return array

# 3/9/2020
def selection(array):
    for i in range(len(array) - 1):
        index = i
        for j in range(i, len(array)):
            if array[i] > array[j]:
                index = j
        tem = array[i]
        array[i] = array[index]
        array[index] = tem
    return array
b = selection([-2, 5, 7, 3, 6])
print(b)
