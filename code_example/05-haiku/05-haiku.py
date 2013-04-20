# rje, 5/07, example 5
# list the words in Windows Haiku
# rje, Python 3

import os
haiku = ''
fp = open("Haiku.txt")
for line in fp:
    haiku += line
print(haiku)
print("\n")
words = haiku.split()
word_list = []
for w in words:
    w = w.strip(' .,;:"!-?')
    w = w.lower()
    word_list.append(w)
word_list.sort()
for a in word_list:
    print(a)
