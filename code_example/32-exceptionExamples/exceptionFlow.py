# try exception flow
# wfp, 11/26

try:
    value = raw_input('Give me a denominator: ')
    denom = int(value)
    print 'The denominator is: ',denom
    result = 10/denom   
    print '10 divided by ',denom,' gives a value: ',result
    
except ValueError:
    print "couldn't convert input to an int"
    
except ZeroDivisionError:
    print "hey, you can't divide by zero"

print 'Here we are at the end'
