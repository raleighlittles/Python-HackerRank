import numpy
N = int(input())
list_A, list_B = [], []
for i in range(0, N):
    list_A.append([x for x in input().split()])
    
for j in range(0, N):
    list_B.append([y for y in input().split()])
    
array_A = numpy.array(list_A, int)
array_B = numpy.array(list_B, int)

# since the problem specifies 'matrix multiplication', we should use matmul() instead of the traditional dot/cross
print(numpy.matmul(array_A, array_B))