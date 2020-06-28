def reverse(st):
    if len(st) == 0:
        return None
    stlist = list(st)
    i = 0
    j = len(st) - 1
    while i < j:
        stlist[i], stlist[j] = stlist[j], stlist[i]
        i += 1
        j -= 1
    return ''.join(stlist)
def reverse1(st):
    if len(st) < 2:
        return st
    stlist = list(st)
    middle = reverse1(st[1:-1])
    # print(middle)
    return stlist[-1] + middle + stlist[0]
def reverse_w(st):
    if len(st) == 0:
        return st
    i = 0
    while 1:
        while i < len(st) and st[i] == ' ':
            i += 1
        j = i
        if i == len(st):
            break
        while j < len(st) and st[j] != ' ':
            j += 1
        # reverse each word
        st = st[:i] + reverse(st[i:j]) + st[j:]

        i = j
    # reverse the whole string
    return reverse(st)
def newreverse(stlist, left, right):
    if right - left < 1:
        return
    while left < right:
        stlist[left], stlist[right] = stlist[right], stlist[left]
        left += 1
        right -= 1
# the length of input string is always even
def shuffle(stlist, left, right):
    if right - left <= 1:
        return
    len = right - left + 1
    midleft = left + len//4
    mid = left + len//2
    midright = left + 3*len//4
    # print([midleft, mid, midright])
    newreverse(stlist, midleft, mid - 1)
    newreverse(stlist, mid, midright - 1)
    newreverse(stlist, midleft, midright - 1)
    # print(''.join(stlist))
    shuffle(stlist, left, left + 2*(midleft - left) - 1)
    shuffle(stlist, left + 2*(midleft - left), right)
    return stlist
def same(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return True
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True
def replacement(stlist, s1, s2):
    if len(stlist) == 0:
        return stlist
    if len(s1) >= len(s2):
        slow = fast = 0
        while fast < len(stlist):
            if same(stlist[fast:fast + len(s1)], s1):
                fast += len(s1)
                for i in range(len(s2)):
                    stlist[slow] = s2[i]
                    slow += 1
            else:
                stlist[fast], stlist[slow] = stlist[slow], stlist[fast]
                slow += 1
                fast += 1
        return stlist[:slow]
    else:
        count = 0
        for i in range(len(stlist) - len(s1)):
            if same(stlist[i:i + len(s1)], s1):
                count += 1
        for i in range(count * (len(s2) - len(s1))):
            stlist.append(' ')
        slow = len(stlist) - 1
        fast = len(stlist) - 1 - count * (len(s2) - len(s1))
        while fast >= 0:
            if same(stlist[fast - len(s1) + 1:fast + 1], s1):
                fast -= len(s1)
                for i in range(len(s2)):
                    stlist[slow] = s2[len(s2) - 1 - i]
                    slow -= 1
            else:
                stlist[fast], stlist[slow] = stlist[slow], stlist[fast]
                slow -= 1
                fast -= 1
        return stlist

def permutation(stlist, index):
    if index == len(stlist):
        print(''.join(stlist))
        return
    swapped = {}
    for i in range(index, len(stlist)):
        if stlist[i] not in swapped:
            stlist[index], stlist[i] = stlist[i], stlist[index]
            permutation(stlist, index + 1)
            stlist[index], stlist[i] = stlist[i], stlist[index]
            swapped[stlist[i]] = 1
def encoding(stlist):
    if len(stlist) <= 1:
        return ''.join(stlist)
    # step1
    slow = fast = 0
    counter = 0
    while fast < len(stlist):
        stlist[slow] = stlist[fast]
        c = 0
        while fast < len(stlist) and stlist[fast] == stlist[slow]:
            fast += 1
            c += 1
        print([stlist[slow], c])
        slow += 1
        if c > 1:
            stlist[slow] = str(c)
            slow += 1
        else:
            counter += 1
    # step2
    final = slow
    for i in range(counter):
        stlist.append(' ')
    slow = slow + counter - 1
    fast = final - 1
    while fast >= 0:
        # add number
        if ord(stlist[fast]) < ord('A'):
            stlist[slow] = stlist[fast]
            slow -= 1
            fast -= 1
        else:
            stlist[slow] = '1'
            slow -= 1
        # add letter
        stlist[slow] = stlist[fast]
        fast -= 1
        slow -= 1
    return ''.join(stlist[:slow])
def longestsubst(stlist, k):
    if len(stlist) <= 1:
        return len(stlist)
    table = {}
    l = 0
    longest = 0
    for r in range(len(stlist)):
        if stlist[r] not in table:
            table[stlist[r]] = 1
        elif table[stlist[r]] < k:
            table[stlist[r]] += 1
        else:
            while stlist[l] != stlist[r]:
                table[stlist[l]] -= 1
                l += 1
            l += 1
        if longest < r - l + 1:
            longest = r - l + 1
        # window = stlist[l:r + 1]
        # print(window)
    return longest
def anagram(stlist, subst):
    # hashmap initializaiton
    table = {}
    for i in range(len(subst)):
        if subst[i] not in table:
            table[subst[i]] = 1
        else:
            table[subst[i]] += 1
    lettersToMatch = len(table)
    # window initialization
    l = 0
    r = len(subst) - 1
    for i in range(len(subst)):
        if stlist[i] in table:
            table[stlist[i]] -= 1
            if table[stlist[i]] == 0:
                lettersToMatch -= 1
    if lettersToMatch == 0:
        print(stlist[l:r + 1])
    # slide window
    while r < len(stlist) - 1:
        if stlist[l] in table:
            if table[stlist[l]] == 0:
                lettersToMatch += 1
            table[stlist[l]] += 1
        l += 1
        r += 1
        if stlist[r] in table:
            table[stlist[r]] -= 1
            if table[stlist[r]] == 0:
                lettersToMatch -= 1
        if lettersToMatch == 0:
            print(stlist[l:r + 1])
def onezero(st, k):
    l = 0
    count = 0
    result = ''
    for r in range(len(st)):
        if st[r] == '0':
            if count < k:
                count += 1
            else:
                while st[l] != '0':
                    l += 1
                l += 1
        if r - l + 1 > len(result):
            result = st[l:r + 1]
    print(result)

test1 = 'zhaoyuehang'
test1n = list(test1)
print(reverse(test1))
print(reverse1(test1))
test2 = 'I love yahoo'
print(reverse_w(test2))
test3 = 'abcdefg1234567'
test3list = list(test3)
print(''.join(shuffle(test3list, 0, len(test3) - 1)))
test4 = 'my name is hang, and all my friends like hang. hang is from my father.'
test4n = list(test4)
print(''.join(replacement(test4n, list('hang'), list('zhaoyuehang'))))
test5 = 'bacc'
test5n = list(test5)
permutation(test5n, 0)
test6 = 'aaabbaacdd'
test6n = list(test6)
print(encoding(test6n))
test7 = 'abafgcdefg'
print(longestsubst(test7, 1))
test81 = 'aabcbaa'
test82 = 'aab'
anagram(test81, test82)
test9 = '0100101010111010101'
onezero(test9, 1)