# faster palindrome 3

import string

my_str = input('Enter a string: ')
my_str = my_str.lower()

#replace whitespace and punctuation with empty string
for bad_char in string.whitespace+string.punctuation:
    my_str=my_str.replace(bad_char,'')

# reverse and compare
if my_str == my_str[::-1]:
    print(my_str,'is a palindrome')
else:
    print(my_str,'is not a palindrome')
