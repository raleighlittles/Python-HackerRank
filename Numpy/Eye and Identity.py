import numpy
dimensions = tuple(map(int, input().split()))
print(numpy.eye(dimensions[0], dimensions[1], k=0))