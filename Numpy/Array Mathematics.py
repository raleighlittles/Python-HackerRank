import numpy
N, M = tuple(map(int, input().split()))

a = numpy.array([input().split() for i in range(0, N)], int)
b = numpy.array([input().split() for j in range(0, N)], int)

print(a+b, a-b, a*b, a//b, a % b, a**b, sep='\n')