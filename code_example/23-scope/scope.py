x='global'

def aFunc():
    x = 'inFunction'
    def bFunc():
        print x
    bFunc()


class myClass(object):
    x = 'inClass'
    def myMethod(self,x='inParam'):
        return x

myInst = myClass()
yourInst = myClass()
yourInst.x = 'inInstance'

print 'x:',x
print 'aFunc:',
aFunc()
print 'myInst.x:',myInst.x
print 'yourInst.x:',yourInst.x
print 'myInst.myMethod():',myInst.myMethod()
print 'yourInst.myMethod():',yourInst.myMethod()




