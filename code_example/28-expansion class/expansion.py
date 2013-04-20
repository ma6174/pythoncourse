# series expansion of pi as a class
# wfp, 11/11/07
# -1**(k+1)/(2*k)-1

import math
import Rational

class Expansion(object):
    def __init__(self,count=5):
        self.piList = []
        self.item = 0
        self.k = 1
        self.genVals(count)
    def __len__(self):
        return len(self.piList)
    def __getitem__(self,indx):
        if indx > len(self.piList):
            raise IndexError
        else:
            return self.piList[indx]
    def __iter__(self):
        self.item=0
        return self
    def next (self):
        if self.item < len(self.piList):
            val = self.piList[self.item]
            self.item += 1
            return val
        else: raise StopIteration
    def sumRationals (self):
        sum = 0
        for v in self.piList:
            print 'sum:',sum,'plus:',v,
            sum = v + sum
           print 'yields:',sum
        return sum
    def piVal(self):
        sum=0
        for v in self.piList:
            sum = sum + float(v)
        return sum
    def genVals (self,count=5):
        while self.k <= count:
            self.piList.append(Rational.Rational(int(math.pow(-1,self.k+1)),(2*self.k)-1))
            self.k+=1

def demo():
    e = Expansion(10)   # constructor
    print 'last element',e[-1]      # last element, through getitem
    print 'length of e',len(e)      # length overload
    for f in e:         # iterate through the list
        print f
    
    print 'sum of the rationals:',e.sumRationals()
    print 'math.pi/4:',math.pi/4,'versus',e.piVal()


    
        
     
