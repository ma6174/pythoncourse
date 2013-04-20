# wfp, 6/8/07
# simple file example

#little snippet to repeatedly ask for a file to open for read
#continues to prompt until a file opens successfully
openedFile = False
while (not openedFile):
    fileName = input("Open what file: ")
    try:
        fileObjIn = open(fileName,"r")
        openedFile = True
    except IOError:
        prin("Bad file name, try again ")
        
# make a new file, keep the extension but change the name
# so that it ends in "Rev". Thus textFile.txt => textFileRev.txt
fileParts = fileName.split(".")
fileObjOut = open(fileParts[0]+"Rev."+fileParts[1],"w")

# write each line in reverse word order
for line in fileObjIn:
    words = line.split()
    words.reverse()
    for w in words:
        fileObjOut.write(w)
        fileObjOut.write(" ")
    fileObjOut.write("\n")
        

fileObjIn.close()
fileObjOut.close()
    



