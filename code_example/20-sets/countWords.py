# wfp, 2/26/08
# wfp, updated names, 10/11
# set example
import string

file_str = raw_input('What file:')
file_obj = open(file_str)

my_set = set()

for line in file_obj:
    line = line.strip()
    word_list = line.split()

# clean up each word, lower case it, add to the set
    for word in word_list:
        word = word.lower()
        word = word.strip(string.punctuation)
        if word:
            my_set.add(word)

file_obj.close()

print 'There were %d words in the file %s'%(len(my_set),file_str)
print '='*10
print 'The words were'
print_cols = 0

# make a list out of the set, which we can then sort
set_list = list(my_set)
set_list.sort()
for word in set_list:
    print '%13s'%word,
    if print_cols == 5:
        print
        print_cols = 0
    else:
        print_cols += 1
