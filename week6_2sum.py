# coursera algoritthm week6 p1
import time
start = time.time()

items = [0 for i in range(1000000)]

fin = open('2sum.txt', 'rt')
lineCount = 0
while True:
    line = fin.readline()
    if not line:
        break
    items[lineCount] = int(line)
    lineCount += 1
fin.close()
print('input ready')
hashspace = 10000000
space = [[] for i in range(hashspace)]
target = [i for i in range(-10000, 10001)]

for i in items:
    key = i % hashspace
    space[key].append(i)
print('hash ready')
count = 0
for i in items:
    print(count)
    count += 1
    find = []
    for j in target:
        need = j - i
        key = need % hashspace
        if need in space[key]:
            find.append(j)
    for k in find:
        target.remove(k)

end = time.time()

print(len(target), end - start)

