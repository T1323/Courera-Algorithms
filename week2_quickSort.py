# corsera algorithm week 2 assignment
import time


fin = open('QuickSort.txt')
input = [int(i) for i in fin]
input2 = input.copy()
input3 = input.copy()

def quickSort(unsort, sIndex, length, type):
    if length <= 1:
        return 0

    if type == 1:
        unsort[sIndex], unsort[sIndex + length - 1] = unsort[sIndex + length - 1], unsort[sIndex]
    elif type == 2:
        f = unsort[sIndex]
        l = unsort[sIndex + length -1]
        mIndex = sIndex + ((length + 1) // 2) - 1
        m = unsort[mIndex]

        if ((l - f) * (l - m) < 0):
            unsort[sIndex], unsort[sIndex + length - 1] = unsort[sIndex + length - 1], unsort[sIndex]
        elif ((m - f) * (m -l) < 0):
            unsort[sIndex], unsort[mIndex] = unsort[mIndex], unsort[sIndex]
    pivot = unsort[sIndex]

    i = sIndex + 1
    j = sIndex + 1
    end = sIndex + length

    while (j < end):
        if unsort[j] < unsort[sIndex]:
            if i != j:
                unsort[j], unsort[i] = unsort[i], unsort[j]
            i += 1
        j += 1

    if sIndex != i - 1:
        unsort[sIndex], unsort[i - 1] = unsort[i - 1], unsort[sIndex]

    cl = quickSort(unsort, sIndex, i - sIndex - 1, type)
    cr = quickSort(unsort, i, end - i, type)

    return length - 1 + cl + cr

startTime = time.time()
answer = quickSort(input, 0, len(input), 0)
endTime = time.time()
print(answer, endTime - startTime, input)

startTime = time.time()
answer = quickSort(input2, 0, len(input2), 1)
endTime = time.time()
print(answer, endTime - startTime, input2)

startTime = time.time()
answer = quickSort(input3, 0, len(input3), 2)
endTime = time.time()
print(answer, endTime - startTime, input3)
