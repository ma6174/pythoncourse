
def c(denom):
    try:
        res=100/denom 
    except ValueError:
        print 'Value Error'
    else:
        return res

def b(denom):
    try:
        res=c(denom)
    except TypeError:
        print 'Type Error'
    else:
        return res


def a(denom):
    try:
        res=b(denom)
    except ZeroDivisionError:
        print 'division by zero error'
    else:
        return res

print a(1)
print a(2)
print a(0)
