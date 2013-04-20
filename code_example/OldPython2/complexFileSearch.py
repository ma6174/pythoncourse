# wfp, 2.20/08
# starting from a given path, look at all files with a particular suffix to see if 
# they contain a particular string. Assumes suffix indicates a text file

import os

def check(root,myStr,suffix,cnt,fLst,dLst):
    for dirName,dirs,files in os.walk(root):
        for f in files:
            if os.path.splitext(f)[1]==suffix:
                cnt += 1
                fd = open(os.path.join(dirName,f),'r')
                fileStr = fd.read()
                if myStr in fileStr:
                    fName = os.path.join(dirName,f)
                    if fName not in fLst:
                        fLst.append(fName)
                    if dirName not in dLst:
                        dLst.append(dirName)
                fd.close()
    return cnt

theStr = raw_input('What string to look for:')
suffix = raw_input('Files with what suffix:')
rootDir = raw_input('Starting from what dir:')
fileLst = []
dirLst = []
cnt = 0

while not os.path.isdir(rootDir):
    print 'Bad directory name, try again'
    rootDir = raw_input('Start from what dir:')

cnt = check(rootDir,theStr,suffix,cnt,fileLst,dirLst)

print 'Looked at %d %s files'%(cnt,suffix)
print 'Found %d directories containing files with %s suffix and target string: %s'%(len(dirLst),suffix,theStr)
print 'Found %d files with %s suffix containing the target string: %s'%(len(fileLst),suffix,theStr)
print '*****Directory List*****'
for d in dirLst:
    print d

print;print '-----File List-----'
for f in fileLst:
    print f
