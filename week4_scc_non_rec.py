# coursera algoritthm week4
import time

class vertice:
    def __init__(self):
        self.next = []
        self.found = False

class graph:
    def __init__(self):
        self.vertice = []

counts = []
lead = 0
gorder = []

def DFS(Graph, index, first, glist):
    vStack =[]
    Graph.vertice[index].found = True
    vStack.append(index)
    for i in Graph.vertice[index].next[::-1]:
        if Graph.vertice[i].found == False:
            if Graph.vertice[i].found == False:
                vStack.append(i)
    while len(vStack)!= 0:
        vi = vStack[-1]
        if Graph.vertice[vi].found == False:
            Graph.vertice[vi].found = True
            for i in Graph.vertice[vi].next[::-1]:
                if Graph.vertice[i].found == False:
                    vStack.append(i)
        else:
            while vi in vStack:
                vStack.remove(vi)
            if (first == True):
                glist.append(vi)
            else:
                glist[vi] = lead

start0 = time.time()
# build Graphs and revGraph
Graph = graph()
revGraph = graph()

fin = open('test.txt', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    edge = [int(i) for i in line.split()]

    while len(Graph.vertice) < edge[0]:
        v = vertice()
        rv = vertice()
        Graph.vertice.append(v)
        revGraph.vertice.append(rv)

    index = edge[0] - 1
    next = edge[1] - 1
    Graph.vertice[index].next.append(next)
fin.close()

SCC = time.time()
print('read file', SCC - start0)
start = time.time()

totalV = len(Graph.vertice)
for i in range(totalV):
    for j in Graph.vertice[i].next:
        revGraph.vertice[j].next.append(i)

REV = time.time()
print('rev', REV - start)
start = time.time()

#  do first DFS
for i in range(totalV):
    if revGraph.vertice[i].found == False:
        DFS(revGraph, i, True, gorder)
    print(i)

fDFS = time.time()
print('fDFS', fDFS - start)
start = time.time()

#do second DFS
gValue = [0 for i in range(totalV)]
for i in gorder[::-1]:
    if Graph.vertice[i].found == False:
        counts.append(0)
        DFS(Graph, i, False, gValue)
        lead += 1
    counts[gValue[i]] += 1

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