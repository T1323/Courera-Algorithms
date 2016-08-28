# corsera algorithm week 3 assignment
import time
import random

class edge():
    def __init__(self, v0, v1):
        self.ori = [v0, v1]
        self.cur = [v0, v1]
    def __str__(self):
        return str(self.ori[0]) + ',' + str(self.ori[1])

startT = time.time()
fin = open('kargerMinCut.txt')
inputStr = [i for i in fin]

min = 1000
count = len(inputStr)
re = []

while count:
    input = []
    vcount = len(inputStr)
    for i in inputStr:
        tmp = [int(j) for j in i.split()]
        v = tmp[0]
        for k in tmp:
            if k > v:
                e = edge(v, k)
                input.append(e)

    while vcount > 2:
        edgeNum = len(input)
        rand = int(random.random() * edgeNum)
        vDel = input[rand].cur[1]
        vMerge = input[rand].cur[0]
        for i in range(len(input) - 1, -1, -1):
            for j in range(2):
                if input[i].cur[j] == vDel:
                    input[i].cur[j] = vMerge
            if input[i].cur[0] == input[i].cur[1]:
                input.remove(input[i])
        vcount -= 1

    if min > len(input):
        min = len(input)
        re = []
        for e in input:
            re.append(e)
    count -= 1

endT = time.time()
print(min, endT - startT)
for j in re:
    print(j)