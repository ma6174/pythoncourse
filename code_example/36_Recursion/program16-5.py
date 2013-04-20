# recursive function to reverse a string

def reverser (aStr):
    # base case
    if len(aStr) == 1:
        return aStr
    # recursive step
       # divide into parts
       # conquer/reassemble

theStr = raw_input("Reverse what string: ")
result = reverser(theStr)
print "The reverse of %s is %s\n" % (theStr,result)

