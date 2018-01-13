import numpy
N, M = tuple(map(int, input().split()))
running_list = []
for i in range(N):
    running_list.append([x for x in input().split()])

my_array = numpy.array(running_list, float)
print( numpy.mean(my_array, axis = 1), numpy.var(my_array, axis= 0), numpy.std(my_array, axis=None), sep='\n' )