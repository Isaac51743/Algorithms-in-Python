import random
def shuffle(array):
    for idx in range(52 - 1): # idx: 0 -> 50
        tem = random.randint(idx, 52 - 1)
        array[idx], array[tem] = array[tem], array[idx]
test = []
for i in range(52):
    test.append(i + 1)
shuffle(test)
print(test)
# -----------------------------------------------------------------------------------
def randomflow(input, t):
    if random.randint(0, t) == 0:
        global solution
        solution = input
testflow = [1, 3, 9, 5, 2, 3, 9, 2, 9, 2]
t = 6
for i in range(t):
    randomflow(testflow[i], i)
print(solution)
# -----------------------------------------------------------------------------------
temmaxidx = []
temmax = None
def randommax(input, t):
    global temmaxidx
    global temmax
    if temmaxidx == [] and temmax == None:
        temmaxidx.append(t)
        temmax = input
    if input == temmax:
        temmaxidx.append(t)
    elif input > temmax:
        temmax = input
        temmaxidx = [t]
    global solution
    solution = temmaxidx[random.randint(0, len(temmaxidx) - 1)]
t = 8
for i in range(t):
    randommax(testflow[i], i)
print(solution)