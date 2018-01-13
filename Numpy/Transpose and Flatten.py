import numpy

inp = input()
N, M = int(inp[0]), inp[1]
running_list = []
for i in range(0, N):
    line = input().split()
    running_list.append([c for c in line])

arr = numpy.array(running_list, int)
print((numpy.transpose(arr)), (arr.flatten()), sep='\n')
