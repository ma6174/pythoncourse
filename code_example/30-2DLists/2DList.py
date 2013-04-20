# simple 2D list
# wfp, 11/19

table = []
for i in range(0,3):
    row = []
    for j in range(i,i+4):
        row.append(j)
    table.append(row)

print table

table[0][2]=123
table[2][0]=456

print table
