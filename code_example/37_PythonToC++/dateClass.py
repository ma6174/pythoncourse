# simple date class
# wfp, 10/24/07

class Date(object):
    def __init__(self,day=1,month=1,year=2000):
        ''' takes day, month and year as named arguments. 2 digits for day, 2 digits
    for month, 4 digits for year'''
        self.monthList=('January','February','March','April','May','June', 'July','August','September','October','November','December')
        self.day = day
        self.month=month
        self.year=year
    
    def printDate(self):
        ''' Print the date in a nice format'''
        print "%s %d, %d" % (self.monthList[self.month - 1],self.day,self.year)
        
    def strUpdate(self,dateStr):
        ''' Takes a string of the form 10/20/2007 (2 digits for month, 2 digits for day,
         4 digits for year) No return value'''
        month,day,year=[int(n) for n in dateStr.split('/')]
        if validDate(day,month,year):
            self.day = day
            self.month = month
            self.year = year
        else:
            print 'invalid date, date not changed'

def validDate(day,month,year):
    ''' very gross check of the size of day, month and year '''
    if 1<= day <=31 and 1<= month <=12 and 0<= year:
        return True
    return False
