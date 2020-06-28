def setKto(num, k, var):
    print(bin(num))
    tem = 1 << (k - 1)
    if var == 1:
        result = tem | num
    elif var == 0:
        tem1 = ~tem
        result = tem1 & num
    else:
        return None
    return result
def power2(num):
    return (num - 1) & num == 0 and num >= 1
# num1 and num2 are positive
def different(num1, num2):
    tem = num1 ^ num2
    i = 0
    count = 0
    while tem >> i != 0:
        if (tem >> i) & 1 == 1:
            count += 1
        i += 1
    return count
def letterunique(word):
    dic = [0] * 8
    for letter in word:
        line = ord(letter) // 32
        num = ord(letter) % 32
        shift = 32 - 1 - num
        if (dic[line] >> shift) & 1 == 0:
            dic[line] = dic[line] | (1 << shift)
        else:
            return False
    return True
def reverse(num):
    print(bin(num))
    length = len(bin(num)) - 2
    for i in range(length):
        num ^= (1 << i)
        # print(bin(num))
    return bin(num)
def reversest(st):
    stlist = list(st)
    i = 0
    j  =len(st) - 1
    while i < j:
        stlist[i], stlist[j] = stlist[j], stlist[i]
        i += 1
        j -= 1
    return ''.join(stlist)
def hex(num):
    result = ''
    while num > 0:
        cur = num % 16
        if cur > 9:
            curst = chr(cur - 10 + ord('A'))
        else:
            curst = str(cur)
        result += curst
        num //= 16
    result += 'x0'
    print(result)
    return reversest(result)
test1 = 1
print(setKto(test1, 3, 1))
print(power2(8))
print(different(1, 5))
print(letterunique('.sfaeg'))
print(reverse(5))
print(hex(10))