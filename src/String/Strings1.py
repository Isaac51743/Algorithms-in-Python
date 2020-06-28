# def removal(st, letters):
#     if len(st) == 0:
#         return st
#     stlist = []
#     for lt in st:
#         stlist.append(lt)
#     # stlist = list(st)
#     i = 0
#     for j in range(len(stlist)):
#         if stlist[j] not in letters:
#             stlist[i], stlist[j] = stlist[j], stlist[i]
#             i += 1
#     result = ''.join(stlist[:i])
#     return result

# def removespace(st):
#     if len(st) == 0:
#         return st
#     stlist = list(st)
#     i = j = 0
#     firstword = False
#     while 1:
#         # move i to the next word
#         while i < len(stlist) and stlist[i] == ' ':
#             i += 1
#         # in the case of i moving to the end
#         if i == len(stlist):
#             break
#         # add a space before all non-second word
#         if firstword:
#             stlist[j] = ' '
#             j += 1
#         # swap i, j
#         while i < len(stlist) and stlist[i] != ' ':
#             stlist[i], stlist[j] = stlist[j], stlist[i]
#             i += 1
#             j += 1
#         firstword = True
#     return ''.join(stlist[:j])

# slow is the position needing to put a accurate value
# def deduplication(st):
#     if len(st) == 0:
#         return st
#     stlist = list(st)
#     slow = 1
#     for fast in range(1, len(stlist)):
#         if stlist[fast] != stlist[slow - 1]:
#             stlist[fast], stlist[slow] = stlist[slow], stlist[fast]
#             slow += 1
#     return ''.join(stlist[:slow])
def deduplicaterepeat(st):
    if len(st) == 0:
        return st
    stlist = list(st)
    stack = []
    i = 0
    while i < len(stlist):
        if stack == [] or stlist[i] != stack[-1]:
            stack.append(stlist[i])
            i += 1
        else:
            while i < len(stlist) and stlist[i] == stack[-1]:
                i += 1
            stack = stack[:-1]
    return ''.join(stack)
# def deduplicaterepeat1(st):
#     if len(st) == 0:
#         return st
#     stlist = list(st)
#     i = -1
#     j = 0
#     while j < len(stlist):
#         if i < 0 or stlist[j] != stlist[i]:
#             i += 1
#             stlist[i], stlist[j] = stlist[j], stlist[i]
#             j += 1
#         else:
#             while j < len(stlist) and stlist[j] == stlist[i]:
#                 j += 1
#             i -= 1
#     return ''.join(stlist[:i + 1])

def hash(cha):
    return ord(cha) - ord('a') + 1
def substring(st1, st2):
    if len(st1) == 0 or len(st2) == 0 or len(st2) > len(st1):
        return None
    stlist1 = list(st1)
    stlist2 = list(st2)
    shift = []
    target = 0
    hashvalue = 0
    for i in range(len(stlist2)):
        target = target + hash(stlist2[i]) * 26 ** i
        hashvalue = hashvalue + hash(stlist1[i]) * 26 ** i
    i = 0
    j = len(stlist2) - 1
    while j < len(st1):
        if i > 0:
            hashvalue = (hashvalue - hash(stlist1[i - 1])) / 26
            hashvalue = hashvalue + hash(stlist1[j]) * 26 ** (len(st2) - 1)
        if hashvalue == target:
            shift.append(i)
        i += 1
        j += 1
    return shift
# 4/11/2020
def removechar(st, ch):
    if len(st) == 0:
        return st
    stlist = list(st)
    i = 0
    j = len(stlist) - 1
    while i <= j:
        if stlist[i] != ch:
            i += 1
        else:
            stlist[i], stlist[j] = stlist[j], stlist[i]
            j -= 1
    return ''.join(stlist[:i])
def removal(st, letters):
    if len(st) == 0:
        return st
    stlist = list(st)
    i = 0
    for j in range(len(stlist)):
        if stlist[j] not in letters:
            stlist[i], stlist[j] = stlist[j], stlist[i]
            i += 1
    return ''.join(stlist[:i])
def removespace(st):
    if len(st) == 0:
        return st
    count = 0
    i = j = 0
    stlist = list(st)
    while 1:
        # 'and' has order: (j < len(stlist)) should at first
        while j < len(stlist) and stlist[j] == ' ':
            j += 1
        if j == len(stlist):
            break
        if count > 0:
            stlist[i] = ' '
            i += 1
        while j < len(stlist) and stlist[j] != ' ':
            stlist[i], stlist[j] = stlist[j], stlist[i]
            i += 1
            j += 1
        count += 1
    return ''.join(stlist[:i])
def deduplication(st):
    if len(st) == 0:
        return st
    stlist = list(st)
    i = 1
    for j in range(1, len(stlist)):
        if stlist[j] != stlist[i - 1]:
            stlist[i], stlist[j] = stlist[j], stlist[i]
            i += 1
    return ''.join(stlist[:i])
def deduplicaterepeat(st):
    if len(st) == 0:
        return st
    stlist = list(st)
    i = -1
    j = 0
    while j < len(stlist):
        if i >= 0 and stlist[i] == stlist[j]:
            while j < len(stlist) and stlist[i] == stlist[j]:
                j += 1
            i -= 1
        else:
            i += 1
            stlist[i], stlist[j] = stlist[j], stlist[i]
            j += 1
    return ''.join(stlist[:i + 1])
test = 'zhaoyuehang is a handsome man'
print(removal(test, ['a', 'o']))
test1 = '   this message      has no extra   space '
test2 = 'thissss messsege     hasss nnno dduppllicatttion'
test3 = 'abbccccbbdeeeefee'
print(removespace(test1))
print(deduplication(test2))
print(deduplicaterepeat(test3))
test4 = 'hzabcbchooifahabcbcfoinabcbce'
test5 = 'abcbc'
print(substring(test4, test5))