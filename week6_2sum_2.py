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
items.sort()
print('input ready')

find = set()
fIndex = 0
bIndex = 1000000 - 1

while(fIndex != bIndex):
    #print([fIndex, bIndex])
    sum = items[fIndex] + items[bIndex]
    if sum < -10000:
        fIndex += 1
    elif sum > 10000:
        bIndex -= 1
    else:
        find.add(sum)
        tmpIndex = bIndex - 1
        tmpSum = items[fIndex] + items[tmpIndex]
        while tmpSum > -10000:
            find.add(tmpSum)
            tmpIndex -= 1
            tmpSum = items[fIndex] + items[tmpIndex]
        fIndex += 1

end = time.time()
print(len(find), end - start)



