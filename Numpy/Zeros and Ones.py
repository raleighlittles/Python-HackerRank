import numpy
numbers = tuple(map(int, input().split()))
print(numpy.zeros(numbers, dtype = numpy.int), numpy.ones(numbers, dtype = numpy.int), sep='\n')
