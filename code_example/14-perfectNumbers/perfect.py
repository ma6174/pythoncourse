#wfp, simple perfect numbers
# 6/6/07

# get the top of the range
max = int(input("Give me the top range to check: "))
perfect_list=[]
deficient_count=0
abundant_count=0

#for each number
for number_int in range (2,max+1):
    factor_list=[]
    # check the factors from 1 to that number and collect them
    for factor in range (1,number_int):
        if number_int%factor==0:
            factor_list.append(factor)
    # sum up the factors
    # sum_int = sum(factor_list)
    sum_int=0
    for n in factor_list:
        sum_int += n
    #classify
    if sum_int == number_int:
        print(number_int," is a perfect number with factors: ",factor_list)
        perfect_list.append(number_int)
    elif sum_int > number_int:
#        print(number_int, " is an abundant number")
        abundant_count +=1
    else:
#        print(number_int," is a deficient number")
        deficient_count +=1

print()
print("SUMMARY")
print("In the range of 2 to ",max," there are")
print(len(perfect_list)," perfect numbers: ",perfect_list)
print(abundant_count," abundant numbers")
print(deficient_count, "deficient numbers")
