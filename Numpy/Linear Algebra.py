import numpy
N = int(input())
running_list = []
for i in range(0, N):
    running_list.append([x for x in input().split()])
    
my_array = numpy.array(running_list, float)
print(numpy.linalg.det(my_array))