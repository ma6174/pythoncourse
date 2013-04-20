# wfp 6/8,
# simple list comprehensives


# collect all the numbers in a string, turn them into a list of integers
myStr = "abcd1234"
myNums = [int(char) for char in myStr if char.isdigit()]
print(myStr,":",myNums)

# collect all pairs where the pair values are not equal
# user provides the range. Result is a list of pairs (tuples)
max= int(input("What is the range of pairs:"))
pairs = [(x,y) for x in range (1,max) for y in range (1,max) if x != y]
print(max,":",pairs)

# take a list of pairs as (Name,score). Collect the names of everyone
# with a score between user-supplied limits
scores = [("Mary",82),("Bill",25),("Fred",95),("Rich",88),
          ("John",75),("Jim",70),("Irving",100),("Tom",90)]
min,max= input("Give me the range of scores, two '-' separated values: ").split("-")
names = [name for name,val in scores if int(min)<=val<=int(max)]
print(scores,":",min,"-",max)
print(names)




    
