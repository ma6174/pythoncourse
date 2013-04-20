# some exception examples
# wfp, 11/26

fName = raw_input('File to open is: ')
try:
    fs = open(fName,'r')
except IOError:
    print 'bad file name, try again'

value = raw_input('Please give me an integer: ')
try:
    result = int(value)
except ValueError:
    print "Value given not an integer"

myStr = raw_input('Please give me two integers, separated by a space: ')
try:
    val1,val2 = myStr.split()
except ValueError:
    print "Didn't get two values"

myDict = {'a':2,'b':3,'c':4}
myKey = raw_input('Add 1 to what key: ')
try:
    myDict[myKey] += 1
except KeyError:
    myDict[myKey] = 1
print myDict

myStr = '1'
myInt = 1
try:
    myStr + myInt
except TypeError:
    print 'type mismatch for operation specified'

    
    
