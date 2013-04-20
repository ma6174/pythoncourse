# personalized exception
# wfp, 11/26

class myException(Exception):
    def __init__(self,val=None):
        Exception.__init__(self) # do the super class init, here it is Exception
        self.val = val
    def __str__(self):
        return str(self.val)

def search(lst,val):
    cnt = 0
    for v in lst:
        if v == val:
            return cnt
        cnt += 1
    raise myException,val
        

myList =[1,3,5,7,9]
for i in range(1,11):
    try:
        indx=search(myList,i)
    except myException,val:
        print val,'is not in',myList
    else:
        print 'Found',i,'at index',indx
        
