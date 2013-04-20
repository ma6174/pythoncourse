
def set_time(time_val,hour=0,min=0,sec=0,*other):
    '''takes a time value (tuple of hour,min,sec) and sets it to the values
       passed in, which all default to 0. Returns the timeVal'''
    temp=time_val
    if hour:
        temp=(hour,temp[1],temp[2])
    if min:
        temp=(temp[0],min,temp[2])
    if sec:
        temp=(temp[0],temp[1],sec)
    if other:
        print 'Extra parameters'
        for e in other:
            print e
    return temp

def main():
    time_val = (10,10,10)
    new_time_val=set_time(time_val,min=20)
    print 'Value is: %s'%str(new_time_val)

    a_time_val = set_time(time_val,20,20,20)
    print 'Value is: %s'%str(a_time_val)

    some_time_val = set_time(time_val,15,15,15,100,200,300)
    print 'Value is: %s',str(some_time_val)

