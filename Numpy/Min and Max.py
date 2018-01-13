import numpy
N, M = map(int, input().split())
running_list = []
for i in range(0, N):
    running_list.append([x for x in input().split()])

my_array = numpy.array(running_list, int)
print(numpy.max(numpy.min(my_array, axis=1), axis=None))
    