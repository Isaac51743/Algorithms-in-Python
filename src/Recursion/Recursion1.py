# 6/28/2020
def fibonacci(index):
    if index == 0 or index == 1:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)

print(fibonacci(4))

# assuming a and b are both integer, return type is double
def aPowerB(a, b):
    if a == 0 and b > 0:
        return 0
    elif a == 0 and b <= 0:
        return None
    elif a != 0 and b < 0:
        return 1/aPowerB(a, -b)
    else:
        # base case
        if b == 1:
            return a
        elif b == 0:
            return 1
        squareRoot = aPowerB(a, b//2)
        if b % 2 == 0:
            return  squareRoot * squareRoot
        else:
            return squareRoot * squareRoot * a

print(aPowerB(-2, -4))