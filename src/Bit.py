def setKthBitTo(number, k, oneOrZero):
    print(bin(number), end=' ')
    shiftedOne = 1 << (k - 1)
    if oneOrZero:
        number = number | shiftedOne
    else:
        shiftedZero = ~shiftedOne
        number = number & shiftedZero
    print(bin(number), end=' ')
    return number

testNumber = 1
print(setKthBitTo(testNumber, 3, 1))

def isPowerTo2(number):
    return number & (number - 1) == 0 and number > 0

print(isPowerTo2(16))

# num1 and num2 are positive
def numberOfDifferentBits(number1, number2):
    XOR = number1 ^ number2
    count = 0
    while XOR > 0:
        XOR = XOR >> 1
        if XOR & 1 == 1:
            count += 1
    return count

print(numberOfDifferentBits(1, 7))

# assuming 32 bit machine
def isLetterunique(word):
    positions = [0] * 8
    for letter in word:
        position = ord(letter) // 32
        shift = 32 - 1 - ord(letter) % 32
        if (positions[position] >> shift) & 1 == 0:
            positions[position] = positions[position] | (1 << shift)
        else:
            return False
    return True

print(isLetterunique('.sfaeg'))

def reverseEveryBit(number):
    print(bin(number), end=' ')
    length = len(bin(number)) - 2
    for shift in range(length):
        number = number ^ (1 << shift)
    return number

print(reverseEveryBit(5))

def hexadecimalRepresentation(number):
    result = []
    while number > 0:
        curPosition = number % 16
        number = number // 16
        if curPosition > 9:
            result.append(chr(curPosition - 10 + ord('A')))
        else:
            result.append(str(curPosition))
    result.append('x')
    result.append('0')
    # reverse
    leftIndex = 0
    rightIndex = len(result) - 1
    while leftIndex < rightIndex:
        result[leftIndex], result[rightIndex] = result[rightIndex], result[leftIndex]
        leftIndex += 1
        rightIndex -= 1
    return ''.join(result)

print(hexadecimalRepresentation(100))