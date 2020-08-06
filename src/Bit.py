def set_kth_bit_to(number, k, one_or_zero):
    print(bin(number), end=' ')
    shifted_one = 1 << (k - 1)
    if one_or_zero:
        number = number | shifted_one
    else:
        shifted_zero = ~shifted_one
        number = number & shifted_zero
    print(bin(number), end=' ')
    return number


def is_power_to_2(number):
    return number & (number - 1) == 0 and number > 0


# num1 and num2 are positive
def number_different_bits(number1, number2):
    xor = number1 ^ number2
    count = 0
    while xor > 0:
        xor = xor >> 1
        if xor & 1 == 1:
            count += 1
    return count


# assuming 32 bit machine
def is_letter_unique(word):
    positions = [0] * 8
    for letter in word:
        position = ord(letter) // 32
        shift = 32 - 1 - ord(letter) % 32
        if (positions[position] >> shift) & 1 == 0:
            positions[position] = positions[position] | (1 << shift)
        else:
            return False
    return True


def reverse_every_bit(number):
    print(bin(number), end=' ')
    length = len(bin(number)) - 2
    for shift in range(length):
        number = number ^ (1 << shift)
    return number


def hexadecimal_representation(number):
    result = []
    while number > 0:
        cur_position = number % 16
        number = number // 16
        if cur_position > 9:
            result.append(chr(cur_position - 10 + ord('A')))
        else:
            result.append(str(cur_position))
    result.append('x')
    result.append('0')

    # reverse
    left_index = 0
    right_index = len(result) - 1
    while left_index < right_index:
        result[left_index], result[right_index] = result[right_index], result[left_index]
        left_index += 1
        right_index -= 1
    return ''.join(result)


testNumber = 1
print(set_kth_bit_to(testNumber, 3, 1))
print(is_power_to_2(16))
print(number_different_bits(1, 7))
print(is_letter_unique('.sfaeg'))
print(reverse_every_bit(5))
print(hexadecimal_representation(100))