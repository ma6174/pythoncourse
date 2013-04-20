# Reverse a string using a recursive function.

def reverse (aStr):
    """Recursive function to reverse a string."""
    print "Got as an argument:",aStr
    # base case
    if len(aStr) == 1:
        print "Base Case!"
        return aStr
    # recursive step
    else:
        newStr =reverse(aStr[1:]) + aStr[0]
        print "Reassembling %s and %s into %s"%(aStr[1:],aStr[0],newStr)
        return newStr

theStr = raw_input("What string: ")
print
resultStr = reverse(theStr)
print "\nThe reverse of %s is %s\n"%(theStr,resultStr)
