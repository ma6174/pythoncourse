# rje, 05/07 Example 4 Assignments
# wfp, 05/31/07, updated:
# wfp, 8/13/11, updated names
# rje, 5/15/12 Python 3
# - include short circuit
# - T/F compares
# - var names
# - str compares

a_bool,b_bool = True, False
c_int,d_int = 3, 8
e_str,f_str = 'z', '5'

print('Booleans a_bool, b_bool: ', a_bool, b_bool)
print('Integers c_int, d_int: ', c_int, d_int)
print('Characters (strings) e_str, f_str: ', e_str, f_str)

print()
print("More on True and False")
print("a_bool== True:", a_bool==True)
print("True == 1:", True == 1)
# remember, anything not false is logically true
print("True == 2:", True == 2)
print("b_bool == False:", b_bool == False)
print("False == 0:", False == 0)
# anything empty is in fact logically false
print("False == []:", False == [])

print()
print("Some Comparison Results, c_int=3, d_int=8, e_str='z', f_str='5'")
print('c_int == d_int: ', c_int == d_int)
print('c_int != d_int: ', c_int != d_int)
print('c_int < 3: ',  c_int < 3)
print('c_int <= 3: ', c_int <= 3)
print('c_int > 3: ',  c_int > 3)
print('c_int >= 3: ', c_int >= 3)
print("e_str == 'z':", e_str == 'z')
print("e_str >= 'a':", e_str >= 'a')
print("f_str >= e_str:", f_str >= e_str)
print("f_str == '5'", f_str == '5')
print("f_str == 5:", f_str == 5)

print()
print("Some Boolean Results: c_int=3 and d_int=8")
print('c_int >= 5 or d_int <= 9: ', c_int >= 5 or d_int <= 9)
print('c_int >= 0 and d_int >= 4: ', c_int >= 0 and d_int >= 4)
print('c_int != d_int or c_int < -6: ', c_int != d_int or c_int < -6)
print('c_int <= 0 and d_int > -6: ', c_int <= 0 and d_int > -6)
print('1 <= c_int and c_int <= 5: ', 1 <= c_int and c_int <= 5)
print('1 <= d_int and d_int <= 5: ', 1 <= d_int and d_int <= 5)

print()
print("Some Short Circuit Results")
print("True or False", True or False)
print("True and False", True and False)
print("2 or 3:", 2 or 3)
print("0 or 3:", 0 or 3)
print("2 and 3:", 2 and 3)
print("3 and 0:", 3 and 0)
print("'' and 3:", '' and 3)


