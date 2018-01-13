import numpy
N, M = tuple(map(int, input().split()))
running_list = []
for i in range(0, N):
    running_list.append(input().split())
    
my_array = numpy.array(running_list, int)
print(numpy.prod(numpy.sum(my_array, axis=0), axis=None))