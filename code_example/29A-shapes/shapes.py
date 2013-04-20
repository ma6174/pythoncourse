# example inheritance heirarchy - shapes
# lkd, 04/20/09; rje 12/02/2011
import math

class shape(object):
    def __init__(self,t="shape"):
        print "In shape __init__:"
        self.tag = t

    def __str__(self):
        print "In shape __str__:"
        return self.tag

    def __repr__(self):
        print "In shape __repr__: "
        return self.__str__()

class polygon(shape):
    def __init__(self,ss,t="polygon"):
        """create polygon, ss gives lengths of sides (at least 3 sides)"""
        print "In polygon __init__"
        shape.__init__(self,t)
        self.sides = ss

    def __str__(self):
        print "In polygon __str__"
        res = shape.__str__(self) +", side lengths: "+\
              " ".join([str(l) for l in self.sides])
        return res

    def perimeter(self):
        print "In polygon perimeter"
        return sum(self.sides)

class triangle(polygon):
    def __init__(self,s1=1,s2=1,s3=1,t="triangle"):
        """create rectangle with sidelengths s1, s2, and s3"""
        polygon.__init__(self, [s1,s2,s3], t)

    def area(self):
        """Heron's Formula"""
        print "In triangle area"
        semip = sum(self.sides)/2.0
        prod = semip*(semip-self.sides[0])*(semip-self.sides[1])*(semip-self.sides[2])
        return math.sqrt(prod)

class rectangle(polygon):
    def __init__(self,w=1,h=1,t="rectangle"):
        """create rectangle of width w and height h"""
        polygon.__init__(self, [w,h], t)

    def __str__(self):
        print "in rectangle __str__"
        res = polygon.__str__(self)+", width: "+str(self.sides[0])+\
              ", height: "+str(self.sides[1])
        return res

    def area(self):
        print "in rectangle area"
        return self.sides[0]*self.sides[1]

##    def perimeter(self):
##        print "in rectangle perimeter"
##        return 2*(self.sides[0]+self.sides[1])

class square(rectangle):
    def __init__(self,l=1,t="square"):
        rectangle.__init__(self,l,l,t)

class circle(shape):
    def __init__(self,r = 1,t = "circle"):
        """create circle, argument gives radius"""
        shape.__init__(self,t)
        self.radius = r

    def __str__(self):
        res = shape.__str__(self) +", radius: "+"%.2f"%self.radius
        return res

    def perimeter(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*self.radius*self.radius

def demo():
    s = shape()
    print "s prints as", s, "\n"

    p = polygon([2,2,2,2,2])
    print "p prints as", p
    print "perimeter of p is %.2f"%p.perimeter(),"\n"

    t = triangle(2,2,3)
    print "t prints as", t
    print "perimeter of t is %.2f"%t.perimeter()
    print "area of t is %.2f"%t.area(), "\n"

    r = rectangle(2,3)
    print "r prints as", r
    print "perimeter of r is %.2f"%r.perimeter()
    print "area of r is %.2f"%r.area(), "\n"

    sq = square(5)
    print "sq prints as", sq
    print "perimeter of sq is %.2f"%sq.perimeter()
    print "area of sq is %.2f"%sq.area(), "\n"

    c = circle()
    print "c prints as", c
    print "perimeter of c is %.2f"%c.perimeter()
    print "area of c is %.2f"%c.area(), "\n"

    # polymorphism at work in the calls to s.perimeter() and s.area()!
    l = [p, t, r, sq, c]
    print "sum of perimeters is %.2f"%sum([s.perimeter() for s in l])
    print "sum of areas is %.2f"%sum([s.area() for s in l])
    
    
