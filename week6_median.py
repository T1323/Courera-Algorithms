# coursera algoritthm week6 p2
import time

def heap_insert(heap, node, mode):
    heap.append(node)
    n = len(heap) - 1

    if mode == 0:
        while n != 0 and heap[n] < heap[(n-1)//2]:
            p = (n - 1) // 2
            [heap[p], heap[n]] = [heap[n], heap[p]]
            n = p
    else:
        while n != 0 and heap[n] > heap[(n-1)//2]:
            p = (n - 1) // 2
            [heap[p], heap[n]] = [heap[n], heap[p]]
            n = p

def heap_get(heap, mode):
    if len(heap) == 0:
        return 0

    ret = heap[0]
    last = len(heap) - 1
    [heap[last], heap[0]] = [heap[0], heap[last]]
    heap.remove(heap[last])
    last -= 1
    n = 0
    if mode == 0:
        while ((n + 1) * 2 <= last and heap[n] > heap[(n + 1) * 2]) or ((n + 1) * 2 - 1 <= last and heap[n] > heap[(n + 1) * 2 - 1]):
            sc = (n + 1) * 2 - 1
            if (n + 1) * 2 <= last and heap[(n + 1) * 2] < heap[(n + 1) * 2 -1]:
                sc = (n + 1) * 2
            [heap[sc], heap[n]] = [heap[n], heap[sc]]
            n = sc
        return ret
    else:
        while ((n + 1) * 2 <= last and heap[n] < heap[(n + 1) * 2]) or ((n + 1) * 2 - 1 <= last and heap[n] < heap[(n + 1) * 2 - 1]):
            sc = (n + 1) * 2 - 1
            if (n + 1) * 2 <= last and heap[(n + 1) * 2] > heap[(n + 1) * 2 -1]:
                sc = (n + 1) * 2
            [heap[sc], heap[n]] = [heap[n], heap[sc]]
            n = sc
        return ret

start = time.time()
heapHigh = []
heapLow = []
totalCount = 0
medianSum = 0
median = []

fin = open('Median.txt', 'rt')

while True:
    line = fin.readline()
    if not line:
        break

    input = int(line)
    totalCount += 1

    if len(heapLow) == 0 or input < heapLow[0]:
        heap_insert(heapLow, input, 1)
    else:
        heap_insert(heapHigh, input, 0)

    if totalCount < 2:
        medianSum += heapLow[0]
        median.append(heapLow[0])
    else:
        while len(heapLow) != ((totalCount + 1) // 2):
            if len(heapLow) > ((totalCount + 1) // 2):
                item = heap_get(heapLow, 1)
                heap_insert(heapHigh, item, 0)
            else:
                item = heap_get(heapHigh, 0)
                heap_insert(heapLow, item, 1)

        medianSum += heapLow[0]
        median.append(heapLow[0])
fin.close()
end = time.time()

print(medianSum % 10000, end - start)

