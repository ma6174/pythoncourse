# rje
# Demo "break" and "else"
# Test a number to see if it is prime
# by checking to see if anything divides into it

# from math import sqrt  # get square root function from math module
import math

n = input('Is this positive integer prime? ')
n = int(n)

# d = int(math.sqrt(n))  # upper limit of possible factors of n
d = n - 1
while d > 1:
    if n % d == 0:        # evenly divisible: found factor
        print(n, ' has factor ', d)
        break             # skip else
    d = d - 1
else:
    print(n, ' is prime. ')

print('Thanks for playing')
