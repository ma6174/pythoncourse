# simple date class
# wfp, 10/24/07
# wfp, 11/11, updated names

class Date(object):
    def __init__(self,day=1,month=1,year=2000):
        ''' takes day, month and year as named arguments. 2 digits for day, 2 digits
    for month, 4 digits for year'''
        print 'Called the Init Method'
        self.month_list=('January','February','March','April','May','June', 'July','August','September','October','November','December')
        self.day = day
        self.month=month
        self.year=year
    
    def print_date(self):
        ''' Print the date in a nice format'''
        print "This is: %s %d %d" % (self.month_list[self.month - 1],self.day,self.year)
        
    def str_update(self,date_str):
        ''' Takes a string of the form 10/20/2007 (2 digits for month, 2 digits for day,
         4 digits for year) No return value'''
        month,day,year=[int(n) for n in date_str.split('/')]
        if valid_date(day,month,year):
            self.day = day
            self.month = month
            self.year = year
        else:
            print 'invalid date, date not changed'

def valid_date(day,month,year):
    ''' very gross check of the size of day, month and year '''
    if 1<= day <=31 and 1<= month <=12 and 0<= year:
        return True
    return False
