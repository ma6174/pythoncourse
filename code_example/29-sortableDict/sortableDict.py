# sortable dictionary
# wfp, 11/4/2007

class sortableDict(dict):
    def __init__(self):
        dict.__init__(self)
        self.tag = 'sortable dictionary'
    def sort(self):
        lst = [(k,v) for k,v in self.items()]
        lst.sort()
        return lst
    def __str__(self):
        res = self.tag+'\n'+dict.__str__(self)
        return res

def demo():
    myDict = sortableDict()
    myDict['bill']=100
    myDict['fred']=50
    myDict['alex']=10
    myDict['laurie']=500
    print myDict
    print
    print myDict.sort()
            
