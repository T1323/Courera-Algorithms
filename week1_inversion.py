# corsera algorithm week 1 assignment
fin = open('IntegerArray.txt')
#input_str = fin.read().split()
input = [int(i) for i in fin]
#print(input)



def getSortAndInversion(input):
    length = len(input)

    if length == 1:
        return 0

    half = length // 2
    input_left = input[:half]
    input_right = input[half:]
    num_left = getSortAndInversion(input_left)
    num_right = getSortAndInversion(input_right)
    num = num_left + num_right
    len_l = len(input_left)
    len_r = len(input_right)
    l = 0
    r = 0
    for i in range(length):
        if (l == len_l):
            input[i] = input_right[r]
            r += 1
        elif (r == len_r):
            input[i] = input_left[l]
            l += 1
        else:
            if (input_left[l] <= input_right[r]):
                input[i] = input_left[l]
                l += 1
            else:
                input[i] = input_right[r]
                r += 1
                num += (len_l - l)
    return num

print(getSortAndInversion(input))



