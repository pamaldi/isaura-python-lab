import numpy as numpy
a = numpy.asarray([1.0, 2.0, 3.0])
print('Array a')
print(*a)
b=2.0
c=a*b
assert c[0] == 2
