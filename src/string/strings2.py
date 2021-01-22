from collections import defaultdict


def reverse_recursive(text_list, left, right):
    if left >= right:
        return ''.join(text_list)
    text_list[left], text_list[right] = text_list[right], text_list[left]
    return reverse_recursive(text_list, left + 1, right - 1)


def reverse_iterative(text):
    if not text:
        return ""
    text_list = list(text)
    left = 0
    right = len(text) - 1
    while left < right:
        text_list[left], text_list[right] = text_list[right], text_list[left]
        left += 1
        right -= 1
    return ''.join(text_list)


def reverse_word(text):
    if not text:
        return ""
    text_list = list(text)
    idx = 0
    while True:
        while idx < len(text_list) and text_list[idx] == " ":
            idx += 1
        if idx == len(text_list):
            break
        start = idx
        while idx < len(text_list) and text_list[idx] != " ":
            idx += 1
        reverse_recursive(text_list, start, idx - 1)
    return reverse_recursive(text_list, 0, len(text_list) - 1)


test_text1 = 'zhao yue hang'
print(reverse_recursive(list(test_text1), 0, len(test_text1) - 1))
print(reverse_iterative(test_text1))
print(reverse_word(test_text1))


def replacement(text, seg1, seg2):
    if not text or not seg1 or not seg2:
        return text
    text_list = list(text)
    if len(seg1) >= len(seg2):
        slow = fast = 0
        while fast < len(text_list):
            if fast <= len(text_list) - len(seg1) and text[fast:fast + len(seg1)] == seg1:
                for letter in seg2:
                    text_list[slow] = letter
                    slow += 1
                fast += len(seg1)
            else:
                text_list[slow] = text_list[fast]
                slow += 1
                fast += 1
        return ''.join(text_list[:slow])
    else:
        count = 0
        for i in range(len(text_list) - len(seg1) + 1):
            if text[i:i + len(seg1)] == seg1:
                count += 1
        fast = len(text_list) - 1
        text_list.extend([" "] * count * (len(seg2) - len(seg1)))
        slow = len(text_list) - 1
        while fast >= 0:
            if fast >= len(seg1) - 1 and text[fast - len(seg1) + 1:fast + 1] == seg1:
                for i in range(len(seg2)):
                    text_list[slow] = seg2[-1 - i]
                    slow -= 1
                fast -= len(seg1)
            else:
                text_list[slow] = text_list[fast]
                slow -= 1
                fast -= 1
        return ''.join(text_list)


test_text2 = 'my name is hang, and all my friends like hang. hang is from my father.'
print(replacement(test_text2, 'hang', 'zhaoyuehang'))
print(replacement(test_text2, 'hang', 'ZYH'))


# the length of input text is always even
def shuffle(text_list, left, right):
    if right - left + 1 < 4:
        return
    chunk1 = left
    chunk2 = left + (right - left + 1) // 4
    chunk3 = left + (right - left + 1) // 2
    chunk4 = left + (right - left + 1) * 3 // 4
    reverse_recursive(text_list, chunk2, chunk3 - 1)
    reverse_recursive(text_list, chunk3, chunk4 - 1)
    reverse_recursive(text_list, chunk2, chunk4 - 1)
    shuffle(text_list, left, left + 2 * (chunk2 - chunk1) - 1)
    shuffle(text_list, left + 2 * (chunk2 - chunk1), right)


test_text3 = list('abcdefg1234567')
shuffle(test_text3, 0, len(test_text3) - 1)
print(''.join(test_text3))


def permutation(text_list, cur_idx):
    if not text_list:
        return
    if cur_idx == len(text_list):
        print(''.join(text_list), end=" ")
        return
    visited = set()
    for i in range(cur_idx, len(text_list)):
        if text_list[i] not in visited:
            visited.add(text_list[i])
            text_list[cur_idx], text_list[i] = text_list[i], text_list[cur_idx]
            permutation(text_list, cur_idx + 1)
            text_list[cur_idx], text_list[i] = text_list[i], text_list[cur_idx]


test_text4 = list('bacc')
permutation(test_text4, 0)
print()


def encode(text):
    if not text:
        return ""
    text_list = list(text)
    slow = fast = 1
    single_num = 0
    while fast < len(text_list):
        if text_list[fast] == text_list[slow - 1]:
            count = 1
            while fast < len(text_list) and text_list[fast] == text_list[slow - 1]:
                fast += 1
                count += 1
            num_str = str(count)
            for letter in num_str:
                text_list[slow] = letter
                slow += 1
        else:
            single_num += 1
            text_list[slow] = text_list[fast]
            slow += 1
            fast += 1
    if single_num > len(text_list) - slow:
        text_list.extend([""] * (single_num - (len(text_list) - slow)))
    fast = slow - 1
    slow = len(text_list) - 1
    while fast >= 0:
        if text_list[fast].isalpha() and (fast == slow - 1 or text_list[fast + 1].isalpha()):
            text_list[slow] = "1"
            slow -= 1
            text_list[slow] = text_list[fast]
            fast -= 1
            slow -= 1
        else:
            text_list[slow] = text_list[fast]
            slow -= 1
            fast -= 1
    return ''.join(text_list[slow + 1:])


test_text7 = 'aaabbaacdd'
print("encoding: ", encode(test_text7))


def find_longest_substring_unique(text):
    if not text:
        return ""
    left = 0
    final_left = final_right = 0
    visited = set()
    for right in range(len(text)):
        if text[right] not in visited:
            visited.add(text[right])
        else:
            while text[left] != text[right]:
                visited.remove(text[left])
                left += 1
            left += 1
        if final_right - final_left < right - left:
            final_left = left
            final_right = right
    return text[final_left:final_right + 1]


def find_longest_substring_k(text, k):
    if not text or k <= 0:
        return ""
    visited = defaultdict(int)
    left = 0
    final_left = final_right = 0
    for right in range(len(text)):
        if visited[text[right]] < k:
            visited[text[right]] += 1
        else:
            while text[left] != text[right]:
                visited[text[left]] -= 1
                left += 1
            left += 1
        if final_right - final_left < right - left:
            final_left = left
            final_right = right
    return text[final_left:final_right + 1]


def find_longest_substring_kzeros(text, k):
    if not text or k <= 0:
        return ""
    zero_num = 0
    left = 0
    final_left = final_right = 0
    for right in range(len(text)):
        if text[right] == "0":
            if zero_num < k:
                zero_num += 1
            else:
                while text[left] != "0":
                    left += 1
                left += 1
        if final_right - final_left < right - left:
            final_left = left
            final_right = right
    return text[final_left:final_right + 1]


test_text5 = '0100101010111010101'
print("longest k zeros: ", find_longest_substring_kzeros(test_text5, 3))
test_text6 = 'abcdebfghijklmn'
print("longest unique: ", find_longest_substring_unique(test_text6))
print("longest k times: ", find_longest_substring_k(test_text5, 2))


def find_anagram(text, segment):
    if not text or not segment or len(segment) > len(text):
        return []
    # complete dictionary
    remain = defaultdict(int)
    for letter in segment:
        remain[letter] += 1
    unique_length = len(remain)
    # check first len(segment) elements
    left = 0
    right = len(segment) - 1
    result = []
    for i in range(left, right + 1):
        if text[i] in remain:
            remain[text[i]] -= 1
            if remain[text[i]] == 0:
                unique_length -= 1
    if unique_length == 0:
        result.append(text[left:right + 1])
    left += 1
    right += 1
    # check rest elements
    while right < len(text):
        # move left
        if text[left - 1] in remain:
            remain[text[left - 1]] += 1
            if remain[text[left - 1]] == 1:
                unique_length += 1
        # remove right
        if text[right] in remain:
            remain[text[right]] -= 1
            if remain[text[right]] == 0:
                unique_length -= 1
        if unique_length == 0:
            result.append(text[left:right + 1])
        left += 1
        right += 1
    return result


test_text8 = 'aabcbaa'
segment = 'aab'
print("find anagram: ", find_anagram(test_text8, segment))

