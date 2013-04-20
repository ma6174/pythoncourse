# Timing and Sorting
# rje 11/28/2007

from time import time
from random import randint

listSize = 10000  # size of list to sort

# timing wrapper with print
def print_timing(func):
    def wrapper(*arg):
        t1 = time()
        res = func(*arg)
        t2 = time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

# timing of 'selection sort' using Python methods min and index
@print_timing
def minSort(L):
    j = 0  # the j index marks start of unsorted part of list
    for x in L:
        m = min(L[j:])        # find min in rest of list (start at j)
        i = L.index(m,j)      # find index of min
        L[i],L[j] = L[j],L[i] # swap current and min
        j+=1 # update sorted/unsorted boundary
    return L

# timing of 'selection sort' using indexing
@print_timing
def indexSort(L):
    for i in range(len(L)):
        m = i
        for j in range(i,len(L)):
            if L[j] < L[m]:
                m = j
        L[i],L[m] = L[m],L[i]
    return L

# timing of 'bubble sort'
@print_timing
def bubbleSort(l):
    "Sorts l in place and returns it."
    for passesLeft in range(len(l)-1, 0, -1):
        for index in range(passesLeft):
            if l[index] > l[index + 1]:
               l[index], l[index + 1] = l[index + 1], l[index]
    return l

# timing of sort using Python's sort method
@print_timing
def pySort(L):
    L.sort()
    return L

# create a list of random numbers, some may be the same
L = [randint(0,100000) for x in range(listSize)]
print L

# copy as L[:] is used so original list L remains unchanged
L1 = minSort(L[:])
#print L1
L2 = indexSort(L[:])
#print L2
L3 = pySort(L[:])
#print L3
L4 = bubbleSort(L[:])
#print L4
    
