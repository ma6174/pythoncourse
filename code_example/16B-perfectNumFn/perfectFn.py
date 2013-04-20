#wfp, better perfect numbers
# 2/15/08
# wfp updated 10/11, naming

def collect_factors(num):
    factor_list=[]
# check the factors from 1 to that number and collect them
    for factor in range (1,num):
        if num % factor==0:
            factor_list.append(factor)
    return factor_list

def classify_value(num,factor_list,result_list):
    sum_factors = sum(factor_list)
    if sum_factors == num:
        result_list[0].append(num)
    elif sum_factors > num:
        result_list[1] +=1
    else:
        result_list[2] +=1

def print_result_list(num,result_list):
    print()
    print( 'In the range of {} to {} there are'.format(2,top-1))
    print()
    print( '{:8s} {:8s} {:8s}'.format('Perfect','Abundant','Deficient'))
    print( '-'*40)
    print( '{:5d} {:8d} {:9d}'.format(len(result_list[0]),result_list[1],result_list[2]))
    print()
    print( 'Factors for the perfect numbers are:')
    for n in result_list[0]:
        print( '{:5d}: {:s}'.format (n,str(collect_factors(n))))

top_str = input('Check up to what number:')
top = int(top_str)
result_list=[[],0,0]    # first is a list of perfects, then counts of deficient and abundant
for num in range(2,top+1):
    factor_list = collect_factors(num)
    classify_value(num,factor_list,result_list)
print_result_list(num,result_list)
    
