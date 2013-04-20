# 06/11, wfp
# simple function intro
# wfp, 10/11, updated for names

# prompt user for a temp. Return it as a float
def get_temp():
    cels_temp = input("Please enter a temperature in degrees Celsius: ")
    return float(cels_temp)

# convert and return
def celsius_to_fahrenheit(cels_temp):
    result = cels_temp * 1.8 + 32.0
    return result

# make a pretty display
def display(cels_temp,fahr_temp):
    print("Original: ",cels_temp)
    print("Equivalent:",fahr_temp)
    print()

# run everything
a_temp = get_temp()
converted_temp = celsius_to_fahrenheit(a_temp)
# print result
display(a_temp,converted_temp)
