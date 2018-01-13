import numpy
polynomial = list(map(float, input().split()))
value = int(input())
print(numpy.polyval(polynomial, value))