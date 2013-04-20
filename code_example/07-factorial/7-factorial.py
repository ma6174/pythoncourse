# rje
# rje, 5/15/12, Python 3
# Demo "while" loop
# Calculate Factorial

# Prompt for an integer
num_str = input('Factorial; enter an integer: ')
num_int = int(num_str)      # convert input to an integer

# Calculate Factorial
# Start with initial condition: 0! = 1
factorial_int = 1

# multiply n times starting with n
# that is: n * (n-1) * (n-2) * ... * 2 * 1
# decrease n each time until n becomes 0
while num_int > 1:
     factorial_int = factorial_int * num_int   # factorial_int *= num_int
     print("Status:, num_int=",num_int," and factorial = ",factorial_int)
     num_int = num_int - 1  # num_int -= 1
     
print(factorial_int)




