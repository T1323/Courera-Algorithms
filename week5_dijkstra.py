# coursera algoritthm week5
import time

class node:
    def __init__(self, dist, index):
        self.dist = dist
        self.index = index

def heap_insert(heap, node):
    heap.append(node)
    n = len(heap) - 1

    while n != 0 and heap[n].dist < heap[(n-1)//2].dist:
        p = (n - 1) // 2
        [heap[p], heap[n]] = [heap[n], heap[p]]
        n = p

def heap_getMin(heap):
    ret = heap[0]
    last = len(heap) - 1
    [heap[last], heap[0]] = [heap[0], heap[last]]
    heap.remove(heap[last])
    n = 0
    while ((n + 1) * 2 < last - 1 and heap[n].dist > heap[(n + 1) * 2].dist) or ((n + 1) * 2 - 1 < last - 1 and heap[n].dist > heap[(n + 1) * 2 - 1].dist):
        sc = (n + 1) * 2 - 1
        if heap[(n + 1) * 2].dist < heap[(n + 1) * 2 -1].dist:
            sc = (n + 1) * 2
        [heap[sc], heap[n]] = [heap[n], heap[sc]]
        n = sc
    return ret

def heap_del(heap, index):
    last = len(heap) - 1
    [heap[last], heap[index]] = [heap[index], heap[last]]
    heap.remove(heap[last])
    last -= 1
    n = index
    while ((n + 1) * 2 < last and heap[n].dist > heap[(n + 1) * 2].dist) or ((n + 1) * 2 - 1 < last and heap[n].dist > heap[(n + 1) * 2 - 1].dist):
        sc = (n + 1) * 2 - 1
        if (n + 1) * 2 < last and heap[(n + 1) * 2].dist < heap[(n + 1) * 2 -1].dist:
            sc = (n + 1) * 2
        [heap[sc], heap[n]] = [heap[n], heap[sc]]
        n = sc

start = time.time()
X = [i + 1 for i in range(200)] # not yet found
C = [] #already found
hlist = [] #node index in the heap
Nodes = [[] for i in range(200)] # vertice data
short = [100000 for i in range(200)] # short path
path = [[] for i in range(200)]
heap = []

fin = open('dijkstraData.txt', 'rt')
lineCount = 0
while True:
    line = fin.readline()
    if not line:
        break
    line = line.split()
    line = line[1:]
    for s in line:
        s = s.split(',')
        n = node(int(s[1]), int(s[0]))
        Nodes[lineCount].append(n)
    lineCount += 1
fin.close()

#start from Node #1
X.remove(1)
C.append(1)
short[0] = 0
for i in Nodes[0]:
    heap_insert(heap, node(i.dist, i.index))
    hlist.append(i.index)
    path[i.index - 1].append(1)

while len(heap):
    #get edge with min distance
    new_node = heap_getMin(heap)
    index = new_node.index
    dist = new_node.dist

    hlist.remove(index)
    short[index - 1] = dist
    X.remove(index)
    C.append(index)
    path[index - 1].append(index)

    for i in Nodes[index - 1]:
        if i.index in X:
            if i.index not in hlist:
                heap_insert(heap, node(i.dist + dist, i.index))
                hlist.append(i.index)
                path[i.index - 1] = path[index - 1].copy()
            else:
                for h in range(len(heap)):
                    if heap[h].index == i.index:
                        if heap[h].dist > i.dist + dist:
                            heap_del(heap, h)
                            heap_insert(heap, node(i.dist + dist, i.index))
                            path[i.index - 1] = path[index - 1].copy()
                        break


ans = [7,37,59,82,99,115,133,165,188,197]
for a in ans:
    print(short[a - 1])
end = time.time()
print(end - start)
#print(short)
#print(path)
















