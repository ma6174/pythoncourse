# rje, updated by wfp 2/18/08m update wfp 10/11, naming
# npr puzzle. Mileages of 6 digits. Find a mileage such that
#   mileage has the last 4 digits a palindrome
#   add 1, last 5 digits are a palindrome
#   add 1, middle 4 digits are a palindrome
#   add 1, whole 6 digits make a palindrome

import time

def test_palindrome1(a_str):
    while len(a_str)>1:
        if a_str[0] != a_str[-1]:
            return False
        a_str = a_str[1:-1]
    return True

def test_palindrome2(a_str):
    if a_str:
        return a_str == a_str[::-1]
    else:
        return False

test_palindrome = test_palindrome1

def mileage_puzzle():
    for mileage in range(100000,1000000):
        digit_list = list(str(mileage))
        if not test_palindrome(digit_list[-4:]):
            continue
        digit_list = list(str(mileage + 1))
        if not test_palindrome(digit_list[-5:]):
            continue
        digit_list = list(str(mileage + 2))
        if not test_palindrome(digit_list[1:-1]):
            continue
        digit_list = list(str(mileage + 3))
        if test_palindrome(digit_list):
            return mileage

def main():
    start = time.time()
    mileage_int = mileage_puzzle()
    end = time.time()
    print('It took:{:.4f}'.format(end-start))
    print('{:20s}:  {}'.format('Last 4 palindrome',mileage_int))
    print('{:20s}:  {}'.format('Last 5 palindrome',mileage_int + 1))   
    print('{:20s}:  {}'.format('Middle 4 palindrome',mileage_int + 2))
    print('{:20s}:  {}'.format('All 6 palindrome',mileage_int + 3))
