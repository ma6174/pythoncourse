# simple rationalNumber class
# wfp, 10/20/07

def gcd(a,b):
    if not a>b:
        a,b=b,a
    while b!=0:
        rem = a%b
        a,b = b,rem
    return a

def lcm (a,b):
    return (a*b/gcd(a,b))

class Rational(object):
    def __init__(self,numer,denom=1):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return str(self.numer)+'/'+str(self.denom)

    def __repr__(self):
        return self.__str__()

    def __add__(self,f):
        if type(f) == int:
            val = Rational(f)
        else:
            val = f
        theLcm = lcm(self.denom,val.denom)
        theSum = (theLcm/self.denom * self.numer)+(theLcm/val.denom * val.numer)
        return Rational(theSum,theLcm)
    
    def __radd__(self,f):
        return self.__add__(f)

    def __iadd__(self,f):
        self=self.__add__(f)
        return self
    
    def __sub__(self,f):
        theLcm = lcm(self.denom,f.denom)
        theDiff = (theLcm/self.denom * self.numer)-(theLcm/f.denom * f.numer)
        return Rational(theDiff,theLcm)

    def __eq__(self,f):
        f1 = self.reduceRational()
        f2 = f.reduce()
        return f1.numer == f2.numer and f1.denom == f2.denom

    def __float__(self):
        return (float(self.numer)/self.denom)

    def reduceRational(self):
        thegcd = gcd(self.numer,self.denom)
        return Rational(self.numer/thegcd,self.denom/thegcd)

def demoRational():
    r1 = Rational(1,2)
    r2 = Rational(1,4)
    print 'r1 + r2:',r1 + r2     # calls add
    print 'r1 + 1:', r1 + 1      # calls add, requires introspection
    print '1 + r1:', 1 + r1      # calls radd, which calls add, with introspection
    r1 += 1                      # doesn't return, changes in place
    print 'r1 after r1 += 1:', r1   # calls iadd if available, otherwise add/radd
    print 'float(r1):',float(r1)    # call the float conversion function
    


