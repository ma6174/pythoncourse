# wfp, 06/14
# wfp updated names, 10/11
# simple sets

a_set = {'a', 'b', 'c', 'd'}
b_set = {'c', 'd', 'e', 'f'}

print("a_set: ",a_set," and b_set: ",b_set)
print("{:s}".format("-"*70))
print("{:13s} {:32s} {:s}".format("Intersection:","a_set & b_set", a_set & b_set))
print("{:13s} {:32s} {:s}".format("Union:","a_set | b_set", a_set | b_set))
print("{:13s} {:32s} {:s}".format("Difference:","a_set - b_set", a_set - b_set))
print("{:13s} {:32s} {:s}".format("Difference:","b_set - a_set", b_set - a_set))
print("{:s}".format("Symmetric"))
print("{:13s} {:32s} {:s}".format("Difference:","a_set ^ b_set", a_set ^ b_set))
print("{:s}".format("Symmetric"))
print("{:13s} {:32s} {:s}".format("Difference:","b_set ^ a_set", b_set ^ a_set))

print()
print()
a_set={'a', 'b', 'c'}
b_set={'a', 'b', 'c', 'd', 'e'}
print("a_set: ",a_set," and b_set: ",b_set)
print("{:s}".format("-"*70))
print("{:13s} {:32s} {}".format("Subset:","a_set < b_set", a_set < b_set))
print("{:13s} {:32s} {}".format("Subset:","b_set < a_set", b_set < a_set))
print("{:13s} {:32s} {}".format("Superset:","a_set > b_set", a_set > b_set))
print("{:13s} {:32s} {}".format("Superset:","b_set > a_set", b_set > a_set))
print("{:13s} {:32s}".format("Adding:","a_set.add('z')"),end = ' ')
a_set.add('z')
print("{:25s}".format(a_set))
print("{:13s} {:32s}".format("Adding:","a_set.add('a')"),end = ' ')
a_set.add('a')
print("{:25s}".format(a_set))
print("{:13s} {:32s}".format("Discard:","a_set.discard('a')"),end = ' ')
a_set.discard('a')
print("{:25s}".format(a_set))
print("{:13s} {:32s}".format("Discard:","a_set.discard('a')"),end = ' ')
a_set.discard('a')
print("{:25s}".format(a_set))

print()
print()
a_set={'a', 'b', 'c'}
b_set={'x','y','z'}
print("a_set: ",a_set," and b_set: ",b_set)
print("{:s}".format("-"*70))
print("{:13s} {:32s}".format("Copy:","b_set=a_set.copy()"),end = ' ')
b_set = a_set.copy()
print("{:20s}" .format (b_set))
print("{:13s} {:32s}".format("Discard:","a_set.discard('a')"),end = ' ')
a_set.discard('a')
print("{:20s}".format(a_set))
print("{:13s} {:32s} {:s}".format("Shallow Copy","print(b_set):",b_set))

print()
print()
a_set={(1,2),(3,4)}
print("a_set: ",a_set," and b_set: ",b_set)
print("{:s}".format("-"*70))
print("{:13s} {:32s}".format("Copy:","b_set=a_set.copy()"),end = ' ')
b_set = a_set.copy()
print("{:20s}" .format (b_set))
print("{:13s} {:32s}".format("Discard:","a_set.discard('a')"),end = ' ')
a_set.discard('a')
print("{:20s}".format(a_set))
print("{:13s} {:32s} {:s}".format("Shallow Copy","print(b_set):",b_set))

