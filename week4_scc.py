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
    Graph.vertice[index].found = True
    for i in Graph.vertice[index].next:
        if Graph.vertice[i].found == False:
            DFS(Graph, i, first, glist)
    if (first == True):
        glist.append(index)
    else:
        glist[index] = lead

start = time.time()
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

totalV = len(Graph.vertice)
for i in range(totalV):
    for j in Graph.vertice[i].next:
        revGraph.vertice[j].next.append(i)

#  do first DFS
for i in range(totalV):
    if revGraph.vertice[i].found == False:
        DFS(revGraph, i, True, gorder)

#do second DFS
gValue = [0 for i in range(totalV)]
for i in gorder[::-1]:
    if Graph.vertice[i].found == False:
        counts.append(0)
        DFS(Graph, i, False, gValue)
        lead += 1
    counts[gValue[i]] += 1

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
print(maxCount, end - start)