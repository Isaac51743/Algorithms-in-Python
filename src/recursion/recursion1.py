# 12/18/2020
def fibonacci(index):
    if index == 0 or index == 1:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)


print(fibonacci(4))


# assuming a and b are both integer, return type is double
def a_power_b(a, b):
    if a == 0 and b <= 0:
        return None
    elif a == 0 and b > 0:
        return 0
    elif a != 0 and b < 0:
        return 1 / a_power_b(a, -b)
    else:
        # base case
        if b == 0:
            return 1
        elif b == 1:
            return a
        # recursive rules
        square_root = a_power_b(a, b // 2)
        if b % 2 == 1:
            return square_root * square_root * a
        else:
            return square_root * square_root


print(a_power_b(-2, -4))