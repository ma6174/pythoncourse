# wfp, 11/7/2007
# introspection example

import math

print 'float is a builtin type. It prints as follows'
print float
print

print 'list is also a builtin type. It prints as follows'
print list
print

print 'what type is math.pi'
print'type(math.pi) prints', type(math.pi)
print

print 'is math.pi a kind of float or list'
print 'isinstance(math.pi,float) prints',isinstance(math.pi,float)
print 'isinstance(math.pi.list) prints', isinstance(math.pi,list)

class myClass(object):
    pass

myInstance = myClass()
print
print 'myClass prints:',myClass
print 'myInstance: type(myInstance):',type(myInstance)
print 'myInstance: isinstance(myInstance,myClass)',isinstance(myInstance,myClass)

def specialDivide(a,b):
    if type(a)==int and type(b)==int:
        return a/b,a%b
    else:
        return a/b,None

print
print specialDivide(5,3)
print specialDivide(5.0,3)
print specialDivide(5.0,3.0)
