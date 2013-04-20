# The obvious, slow way

import string

my_str = input('Enter a string to check: ')
front=0
end=len(my_str)-1
my_str = my_str.lower()
good_letters_str = string.ascii_lowercase + string.digits
while front<end:
    # ignore whitespace and punctuation
    while not my_str[front] in good_letters_str:
        front +=1
    while not my_str[end] in good_letters_str:
        end -= 1
    if my_str[front] != my_str[end]:
        print(my_str,'is not a palindrome')
        break  # no need to continue, we know now
    front+=1
    end-=1
else:
    print(my_str,'is a palindrome')
