# timed palindromes
# time a function using time.time() and the a @ function decorator
# wfp, updated 9/21/11, naming

import time
import string
import random

def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print('{} took {:0.3f} ms'.format(func.__name__, (t2-t1)*1000.0))
        return res
    return wrapper

@print_timing
def pal_reverse(my_str):
    my_str = my_str.lower()
    for bad_char in string.whitespace + string.punctuation:
        my_str = my_str.replace(bad_char,'')
    return my_str == my_str[::-1]

@print_timing
def pal_walk(my_str):
    front = 0
    end = len(my_str) - 1
    my_str = my_str.lower()
    good_letters = string.ascii_lowercase + string.digits
    while front < end:
        while not my_str[front] in good_letters:
            front += 1
        while not my_str[end] in good_letters:
            end -= 1
        if my_str[front] != my_str[end]:
            return False
        front += 1
        end -= 1
    return True

@print_timing
def pal_walk2(my_str):
    front = 0
    end =len(my_str) - 1
    mid  = len(my_str)//2
    for bad_char in string.whitespace + string.punctuation:
        my_str=my_str.replace(bad_char,'')
    for a_char in my_str:
        if a_char != my_str[end]:
            return False
        end -= 1
        if end < mid:
            return True


def __Pal(x):
    return True if len(x)<= 1 else False if x[0] != x[-1] else __Pal(x[1:-1])

@print_timing
def recurse_pal(x):
    return __Pal(list(filter( lambda x : x in string.ascii_lowercase, x)))


def make_pal(size_int):
    random_obj = random.Random()
    letters = string.ascii_letters
    my_str = ''
    for num in range(0, size_int//2):
        indx = random_obj.randint(0, len(letters) - 1)
        my_str += letters[indx]
    my_str += my_str[::-1]
    return my_str


