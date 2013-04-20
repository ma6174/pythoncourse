# numpy arrays
# wfp, 11/19

import numpy

myArray=numpy.array([1,2,3])
print myArray.ndim
print myArray.dtype
print myArray.shape
print myArray.size

twodArray=numpy.array([(1,2,3,4),(5,6,7,8)])
print twodArray

reshapeArray = numpy.arange(20)
print reshapeArray
reshapeArray=reshapeArray.reshape(4,5)
print reshapeArray

print myArray + 1
print myArray * 2

zArray=numpy.zeros((3,5),numpy.int32)
fArray=numpy.ones((4,2),numpy.float)
print fArray
print zArray
