# corsera algorithm week 3 assignment
import time
import random

def KargerMinCut(graph):
    vcount = len(graph)
    vertice = [i for i in range(vcount)]
    while vcount > 2:
        n1 = vertice[int(random.random() * vcount)]
        rand = int(random.random() * len(graph[n1]))
        n2 = graph[n1][rand]

        for i in graph[n2]:
            if i != n1:
                graph[n1].append(i)
                graph[i].append(n1)
                if n2 in graph[i]:
                    graph[i].remove(n2)
                else:
                    print("error")

            else:
                if n2 in graph[n1]:
                    graph[n1].remove(n2)
                else:
                    print('error')
        graph[n2] = []
        vertice.remove(n2)
        vcount -= 1
    return len(graph[vertice[0]])

start = time.time()

fin = open('kargerMinCut.txt')
inputStr = [i for i in fin]
input = []
for i in range(len(inputStr)):
    #tmp = inputStr[i].split()
    v = [int(j) - 1 for j in inputStr[i].split()]
    v.remove(v[0])
    input.append(v)

min = 1000
n = len(input)
for i in range(n):
    g = []
    for j in range(n):
        element = input[j].copy()
        g.append(element)

    tmp = KargerMinCut(g)
    if tmp < min:
        min = tmp
end = time.time()
print(min, (end - start))


