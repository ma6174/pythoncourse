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
        theLcm = lcm(self.denom,f.denom)
        theSum = (theLcm/self.denom * self.numer)+(theLcm/f.denom * f.numer)
        return Rational(theSum,theLcm)

    def __sub__(self,f):
        theLcm = lcm(self.denom,f.denom)
        theDiff = (theLcm/self.denom * self.numer)-(theLcm/f.denom * f.numer)
        return Rational(theDiff,theLcm)

    def __eq__(self,f):
        f1 = self.reduceRational()
        f2 = f.reduceRational()
        return f1.numer == f2.numer and f1.denom == f2.denom

    def reduceRational(self):
        thegcd = gcd(self.numer,self.denom)
        return Rational(self.numer/thegcd,self.denom/thegcd)

def demoRational():
    r1 = Rational(1,2)          # constructor
    r2 = Rational(1,4)          # constructor
    print 'r1:',r1              # calls str method
    print 'r1 + r2:',r1+r2      # calls add, then str
    print 'r1 - r2:',r1-r2      # calls sub, then str
    print 'r1 == r2:',r1==r2    # calls eq
    


