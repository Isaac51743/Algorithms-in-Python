# 1/15/2021
def char_removal1(text, char_set):
    if len(text) == 0:
        return ''
    text_list = list(text)
    slow = 0
    for fast in range(len(text_list)):
        if text_list[fast] not in char_set:
            text_list[slow], text_list[fast] = text_list[fast], text_list[slow]
            slow += 1
    return ''.join(text_list[:slow])


# unordered, method like quick sort
# this method is used to divided the list into two parts.
def char_removal2(text, char_set):
    if len(text) == 0:
        return ''
    text_list = list(text)
    left = 0
    right = len(text_list) - 1
    while left <= right:
        if text_list[left] not in char_set:
            left += 1
        else:
            text_list[left], text_list[right] = text_list[right], text_list[left]
            right -= 1
    return ''.join(text_list[:left])


def space_removal(text):
    if not text:
        return ""
    text_list = list(text)
    slow = fast = 0
    word_count = 0
    while True:
        while fast < len(text_list) and text_list[fast] == " ":
            fast += 1
        if fast == len(text_list):
            break
        if word_count > 0:
            text_list[slow] = " "
            slow += 1
        while fast < len(text_list) and text_list[fast] != " ":
            text_list[slow] = text_list[fast]
            slow += 1
            fast += 1
        word_count += 1
    return ''.join(text_list[:slow])


test_text1 = '   zhaoyuehang is a     handsome man  '
print(char_removal1(test_text1, {'a', 'o'}))
print(char_removal2(test_text1, {'a', 'o'}))
print(space_removal(test_text1))


def deduplication(text):
    if not text or len(text) == 1:
        return text
    t_list = list(text)
    slow = 1
    for fast in range(1, len(t_list)):
        if t_list[fast] != t_list[slow - 1]:
            t_list[slow] = t_list[fast]
            slow += 1
    return ''.join(t_list[:slow])


def duduplication(text):
    if not text or len(text) == 1:
        return text
    t_list = list(text)
    slow = fast = 1
    while fast < len(t_list):
        while fast < len(t_list) and t_list[fast] == t_list[slow - 1]:
            fast += 1
        if fast == len(t_list):
            break
        t_list[slow] = t_list[fast]
        slow += 1
        fast += 1
    return ''.join(t_list)


def deduplication_re(text):
    if not text or len(text) == 1:
        return text
    stack_top = 0
    t_list = list(text)
    i = 1
    while i < len(t_list):
        if stack_top >= 0 and t_list[i] == t_list[stack_top]:
            while i < len(t_list) and t_list[i] == t_list[stack_top]:
                i += 1
            stack_top -= 1
        else:
            stack_top += 1
            t_list[stack_top] = t_list[i]
            i += 1
    return ''.join(t_list[:stack_top + 1])


test_text2 = 'thissss messsege     hasss nnno dduppllicatttion'
print(deduplication(test_text2))
test_text3 = 'zbbccccbbyeeeehee'
print(deduplication_re(test_text3))


def my_hash(text, start, end, hash_val):
    return (hash_val - (ord(text[start - 1]) - ord("a"))) // 26 + (ord(text[end]) - ord("a")) * 26 ** (end - start)


# assuming lower case letter
def find_substring(text, seg):
    if not text or not seg or len(text) < len(segment):
        return []
    hash_val = 0
    target_val = 0
    for i in range(len(seg)):
        hash_val += (ord(text[i]) - ord("a")) * 26 ** i
        target_val += (ord(seg[i]) - ord("a")) * 26 ** i
    result = []
    if hash_val == target_val:
        result.append(0)
    for i in range(1, len(text) - len(seg) + 1):
        hash_val = my_hash(text, i, i + len(seg) - 1, hash_val)
        if hash_val == target_val:
            result.append(i)
    return result


testText4 = 'hzabcbchooifahabcbcfoinabcbce'
segment = 'abcbc'
print(find_substring(testText4, segment))


