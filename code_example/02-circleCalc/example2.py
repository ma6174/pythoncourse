# wfp, 5/30/07, wfp: updated 9/5/11; rje 5/14/12
# prompt user for the radius, give back the circumference and area

import math

radius_str = input("Enter the radius of your circle:")
radius_float = float(radius_str)

circumference_float = 2 * math.pi * radius_float
area_float = math.pi * radius_float * radius_float
# also, area = math.pi * math.pow(radius_float,2)
# also, area = math.pi * radius_float ** 2

print()
print("The cirumference of your circle is:",circumference_float,\
      ", and the area is:",area_float)
