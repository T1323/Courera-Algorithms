# coursera algoritthm week4
import time

class vertice:
    def __init__(self):
        self.next = []
        self.found = False
        self.value = 0

class graph:
    def __init__(self):
        self.vertice = []
        self.order= []

counts = []
lead = 0

def DFS(Graph, index):
    Graph.vertice[index].found = True
    for i in Graph.vertice[index].next:
        if Graph.vertice[i].found == False:
            DFS(Graph, i)
    Graph.order.append(index)
    Graph.vertice[index].value = lead

start = time.time()
# build Graphs and revGraph
Graph = graph()
revGraph = graph()

fin = open("SCC.txt")
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

totalV = len(Graph.vertice)
for i in range(totalV):
    for j in Graph.vertice[i].next:
        revGraph.vertice[j].next.append(i)

#  do first DFS
for i in range(totalV):
    if revGraph.vertice[i].found == False:
        DFS(revGraph, i)

#do second DFS
for i in revGraph.order[::-1]:
    if Graph.vertice[i].found == False:
        counts.append(0)
        DFS(Graph, i)
        lead += 1
    counts[Graph.vertice[i].value] += 1

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