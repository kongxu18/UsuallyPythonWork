import numpy

a = numpy.array([1, 2, 3, 4, 5])
b = numpy.array([2, 1, 3, 5, 4])
c = a > b
print(c)

d = [5, 2, 3,4]
e = [2, 1, 2]
print(d > e)


a = numpy.ones(shape=(10))

a = a.astype(dtype=numpy.str)
print(a,a.dtype)