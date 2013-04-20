# Timing and Searching
# rje 11/28/2007

from time import time
from random import randint

listSize = 10000  # size of list to search

# timing wrapper with print
def print_timing(func):
    def wrapper(*arg):
        t1 = time()
        res = func(*arg)
        t2 = time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

# timing of binary search
# assumes list 'l' is sorted
@print_timing
def binary_search(l, value):
    # search region from lo to hi
    lo, hi = 0, len(l)-1
    while lo <= hi:    # done when hi index get lower than lo index
        mid = (lo + hi) / 2  # find middle index of region from lo to hi
        if l[mid] < value:   # value is to the right
            lo = mid + 1     # so adjust lo up
        elif value < l[mid]: # value is to the left
            hi = mid - 1     # so adjust hi down
        else:
            return mid       # found it
    return NOT_FOUND

# timing of linear search
# search from beginning until it is found
@print_timing
def linear_search(l, value):
    for i in range(len(l)):
        if l[i] == value:
            return i
    return NOT_FOUND

# timing of Python's search
# use Python's index method
@print_timing
def python_search(l,value):
    try:
        i = l.index(value)
        return i
    except IndexError:
        return NOT_FOUND
    

# create a list of random numbers, some may be the same
L = [randint(0,100000) for x in range(listSize)]
L.sort()  # binary search requires sorted list
print L

# get a random value from list to search for
value = L[randint(0,len(L))]
print "Searching for: ", value

index = binary_search(L,value)
print "Search result: ", index

index = linear_search(L,value)
print "Search result: ", index

index = python_search(L,value)
print "Search result: ", index
