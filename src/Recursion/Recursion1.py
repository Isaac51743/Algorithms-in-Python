# 1/8/2020
# Fibonacci
# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     return fibonacci(num - 1) + fibonacci(num - 2)

# 1/30/2020
# def fibonacci(num):
#     if num == 0 or num == 1:
#         return num
#     else:
#         result = fibonacci(num - 1) + fibonacci(num - 2)
#         return result
# 3/10/2020
def fibonacci(num):
    if num == 0 or num == 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(4))


# 2^n, assume: n>=0
# solution1
# def power(a, b):
#     if b == 1:
#         return a
#     elif b == 0:
#         return 1
#     return a * power(a, b - 1)

# assuming a ≠ 0, b >= 0
# # solution2
def power2(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    tem = power2(a, b//2)
    if b % 2 == 0:
        return tem * tem
    else:
        return tem * tem * a

result = power2(-2, 3)
print(result)