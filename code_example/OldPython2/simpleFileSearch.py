# wfp, 2/19/08
# simple file search

import os

fName = raw_input('What file:')
rootStr = raw_input('Where to start:')
Found = False

if not rootStr:
    rootStr = '/'

for name,dirs,files in os.walk(rootStr):
    if fName in files:
        print 'Found %s in directory %s'% (fName,name)
        Found = True
        break

if not Found:
    print "Couldn't find %s starting from %s"%(fName,rootStr)


