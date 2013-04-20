# wfp, 06/12/07
# string formatting
# wfp updated 9/21/11, naming

import math

# assign a string, print it
my_str = "{} is {} years old".format("Bill",25)
print(my_str)

# note the truncation on %d
pi_float = math.pi
print("Different formats for pi are: {0:e}, {0:f}, {0:%}".format(pi_float))

# 4 decimal points of precision
print("{0:f} versus 4 decimal points of precision, rounded {0:.4f}".format(pi_float))

#left and right justify
print("{0:10s} is left justified; {0:>10s} is right justified".format("Bill"))

# print a column of numbers, right justified
print()
print("Column of numbers")
for num in range (995,1005):
    print("{:6d}".format(num))

# print a pretty table
scores = [("Mary",82),("Bill",25),("Fred",95),("Rich",88),
          ("John",75),("Jim",70),("Irving",100),("Tom",90)]
# header
print()
print("{}".format("="*20))
print("Table 1: Scores")
print()
print("{:8s}   {:5s}".format("NAME","SCORE"))
print("{:8s}   {:5s}".format('-'*4,'-'*5))

#print the scores 
for pair in scores:
    print("{0[0]:8s} : {0[1]:4d}".format(pair))

#footer
print("{}".format("="*20))
    


