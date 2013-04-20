# rje
# Test a number to see if it is prime
# by checking to see if anything divides into it
# update 9/19/11 wfp (naming)
# update 5/15/12 rje Python 3

import math # get square root function from math module

while True:
    num_str = input('Is this positive integer prime? ')
    num_int = int(num_str)
    if num_int > 1 :
        break
    print("Error: input not positive; try again.")


divisor_int = int(math.sqrt(num_int))  # upper limit of possible factors of n

while divisor_int > 1:
    if num_int % divisor_int == 0:   # evenly divisible: found factor
        print(num_int, ' has factor ', divisor_int)
        break                        # skip else
    divisor_int = divisor_int - 1
else:
    print(num_int, ' is prime. ')

print('Thanks for playing')
