# 2. faster than palindrome 1

import string
my_str = input('Enter a string: ')

# remove whitespace and punctuation:
#   replace whitespace and punctuation with empty string
for bad_char in string.whitespace + string.punctuation:
    my_str = my_str.replace(bad_char,'')
    
my_str = my_str.lower()
front = 0
end = len(my_str)-1
mid = len(my_str)/2

for char_str in my_str:
    if char_str != my_str[end]:
        print(my_str,'is not a palindrome')
        break
    end -= 1
    # end just passed the middle. We're done
    if end < mid:
        print(my_str,'is a palindrome')
        break
