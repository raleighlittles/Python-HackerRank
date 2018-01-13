import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)

print(numpy.inner(A,B), numpy.outer(A,B), sep='\n')