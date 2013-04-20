
def fn1 (arg1=[], arg2=27):
    arg1.append(arg2)
    return arg1

my_list = [1,2,3]

print fn1(my_list,4)

print fn1()
print fn1()
print fn1(my_list)
