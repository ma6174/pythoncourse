# wfp 11/5/07
# simple note class

import math
import winsound

class Note(object):
    def __init__(self,octave=4,pitch=9,beats=4):
        self.octave = octave
        self.pitch = pitch
        self.beats = beats
    def hertz(self):
        return 440.0*math.pow(2,(self.octave-4)+(self.pitch-12)/12.0)
    def __str__(self):
        theStr=str(self.octave)+'.'+str(self.pitch)+':'+str(self.beats)
        return theStr

class Song(object):
    def __init__(self,lst=[],oneBeat=250):
        self.noteList = lst
        self.oneBeat=oneBeat 
    def addNote(self,n):
        self.noteList.append(n)
    def processFile(self,fname):
        self.noteList=[]
        fs = open(fname,'r')
        for line in fs:
            temp = line.split()
            d = int(temp[1])
            o = int(temp[0].split('.')[0])
            p = int(temp[0].split('.')[1])
            self.noteList.append(Note(o,p,d))
    def __str__(self):
        retStr=''
        count = 0
        for n in self.noteList:
            retStr = retStr + ' ' + str(n)
            count += 1
            if count == 9:
                count = 0
                retStr += '\n'
        return retStr
    def play(self):
        # windows only
        for n in self.noteList:
            winsound.Beep(int(n.hertz()),n.beats*self.oneBeat)


def demo():
    n1 = Note()
    n2 = Note(octave=5)
    print n1,n2
    s = Song()
    s.addNote(n1)
    s.addNote(n2)
    print s
    # if this is windows, then
    s.play()
    s.processFile('notes.txt')
    s.print
    # if this is windows, then
    s.play()
    
            
    
    
        
