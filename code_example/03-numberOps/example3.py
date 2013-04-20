# example3.py, wfp, 5/3/07. wfp 9/5/11 updated names
# some simple examples of number manipulations
# wfp, 1/3/13, to py3

import math

a_int = 3
b_int = 4
c_int = 5

# we can chain multiple assignments onto one line separated by a ";"
x_float = 6.5; y_float= 9.5

print("Integer computations")
# a print with no string just prints a new line
print()
print(a_int, " + ", b_int, " equals ", a_int + b_int)
print(a_int, " - ", b_int, " equals ", a_int - b_int)
print(a_int, " * ", b_int, " equals ", a_int * b_int)
# division is always a float % gets the remainder
print(a_int, " / ", b_int, " equals ", a_int / b_int)
# integer division done with //
print(a_int, " // ", b_int, " equals ", a_int//b_int," remainder ", a_int % b_int)
print()
print(c_int, " + ", 5, " equals ", c_int + 5) 
print(c_int, " - ", 5, " equals ", c_int - 5)
print(c_int, " * ", 5, " equals ", c_int * 5)
print(c_int, " / ", 5, " equals ", c_int / 5, " remainder ", c_int % 5)

print()
print("Real number computations")
print()
print(x_float, " + ", y_float, " equals ", x_float + y_float)
print(x_float, " - ", y_float, " equals ", x_float - y_float)
print(x_float, " * ", y_float, " equals ", x_float * y_float)
print(x_float, " / ", y_float, " equals ", x_float / y_float)

print()
print("Mixed computations ")
print()
# note that the integer is "promoted" to a float
print(a_int, " - ", x_float, " equals ", a_int - x_float)
print(a_int, " / ", x_float, " equals ", a_int / x_float)

print()
print("Compound Computations, precedence")
print(a_int,"+",b_int,"/",c_int," equals",a_int+b_int/c_int)
print("(",a_int,"+",b_int,")/",c_int," equals ",(a_int+b_int)/c_int)

print()
print("Simple Type Conversion")
print("Value of a_int is:",a_int)
# note that the value of a_int is not changed, but a new float value is returned!
print("Value of float(a_int) is:",float(a_int))
print("Value of x_float is:",x_float)
# again, x_float not changed but the returned value loses information
print("Value of int(x_float) is:",int(x_float))

