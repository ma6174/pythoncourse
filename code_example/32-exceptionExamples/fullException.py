# all aspects of exceptions
# wfp, 11/26

def processFile(fs):
    cnt = 1
    for ln in fs:
        print 'Line '+str(cnt)+':'+ln.strip()
        cnt += 1

fs = ''
while True:
    fName = raw_input('Please give me a file to open: ')
    try:
        fs = open(fName)
    except IOError:
        print 'Bad file name, try again'
#        continue       # continue is redundant
    else:
        print 'Processing the file',fName
        processFile(fs)
        break
    finally:
        if type(fs)==file:
            fs.close()
            print 'finished the file example'
        else:
            print 'going around again'

print 'Line after the try/except block'
    
