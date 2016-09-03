# coursera algoritthm week4
import time

start0 = time.time()
# build Graphs and revGraph
Graph = {}
revGraph = {}

fin = open('SCC.txt', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    edge = [int(i) for i in line.split()]

    while len(Graph) < max(edge):
        Graph[len(Graph)] = []
        revGraph[len(revGraph)] = []

    index = edge[0] - 1
    next = edge[1] - 1
    Graph[index].append(next)
fin.close()

SCC = time.time()
print('read file', SCC - start0)
start = time.time()

totalV = len(Graph)
for i in range(totalV):
    for j in Graph[i]:
        if j in revGraph:
            revGraph[j].append(i)
        else:
            revGraph[j] = [i]

for i in range(totalV):
    Graph[i] = set(Graph[i])
    revGraph[i] = set(revGraph[i])

REV = time.time()
print('rev', REV - start)
start = time.time()

found = [False for i in range(totalV)]
counts = []
lead = 0

def DFS(Graph, index, first, glist, c):
    vStack ={}
    vCount = 1
    vStack[vCount] = index

    while vCount > 0:
        vi = vStack[vCount]
        found[vi] = True
        leave = False
        for i in Graph[vi]:
            if found[i] == False:
                vCount += 1
                vStack[vCount] = i
                leave = True
                break
        if leave:
            continue

        del vStack[vCount]
        vCount -= 1
        if (first == True):
            glist[c[0]] = vi
            c[0] += 1
        else:
            glist[vi] = lead


#  do first DFS
c = [0]
gorder = [0 for i in range(totalV)]
for i in range(totalV):
    if found[i] == False:
        DFS(revGraph, i, True, gorder, c)

fDFS = time.time()
print('fDFS', fDFS - start)
start = time.time()

#do second DFS
gValue = [0 for i in range(totalV)]
found = [False for i in range(totalV)]
for i in gorder[::-1]:
    if found[i] == False:
        counts.append(0)
        DFS(Graph, i, False, gValue, c)
        lead += 1
    counts[gValue[i]] += 1

#counts = [gValue.count(i) for i in set(gValue)]

sDFS = time.time()
print('sDFS', sDFS - start)
start = time.time()

maxCount = [0, 0, 0, 0, 0]

length = min([len(counts),5])
for k in range(length):
    m = max(counts)
    if m != 0:
        maxCount[k] = m
        counts.remove(m)
    else:
        break

end = time.time()
print(maxCount, end - start, end - start0)