from math import pi

class Circle (object):
    ''' only allows setting radius. When radius is set, area and circumference
        are updated. Neither area nor circumference can be set
    '''
    def __init__(self, rad=1):
        self.__radius = rad
        self.__circumference = 2*pi*rad
        self.__area = rad*rad*pi
    def getRadius(self):
        return self.__radius
    def setRadius(self,rad):
        self.__radius = rad
        self.__circumference = 2*pi*rad
        self.__area = rad*rad*pi
    def getArea(self):
        return self.__area
    def getCircumference(self):
        return self.__circumference
    radius = property(fget=getRadius,fset=setRadius)
    circumference = property(fget=getCircumference)
    area = property(fget=getArea)
    def __str__(self):
      return 'Radius=%.2f, Circumference=%.2f, Area=%.2f\n'% \
              (myC.radius, myC.area, myC.circumference)  

myC = Circle(10)
print 'My Circle is:',myC
myC.radius=5
print 'My Circle is:',myC
myC.circumference=10

