# wfp, 2/26/08
# wfp, updated 10/11, naming
# dictionary example
import string

def get_words(f_obj,my_dict):
    for line in f_obj:
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            word = word.lower()
            word = word.strip(string.punctuation)
            if word:
                if word in my_dict:
                    my_dict[word]+=1
                else:
                    my_dict[word]=1

def print_alphabetic(my_dict):
    # pairs_list = [(key,value) for key,value in my_dict.items()]
    pairs_list = []
    for key,value in my_dict.items():
        pairs_list.append((key,value))
    # print pairs
    print('+'*12)
    print('Words in alphabetical order as word:count pairs')
    pairs_list.sort()
    print_cols = 0
    for word,cnt in pairs_list:
        print('{:13s}:{:3d}'.format(word,cnt),end=' ')
        if print_cols == 3:
            print()
            print_cols = 0
        else:
            print_cols += 1

def print_frequency(my_dict):
    #pairs_list = [(value,key) for key,value in my_dict.items()]
    pairs_list = []
    for key,value in my_dict.items():
        pairs_list.append((value,key))
    print()
    print('+'*12)
    print('Words in frequency order as count:word pairs')
    pairs_list.sort(reverse=True)
    print_cols = 0
    for cnt,word in pairs_list:
        print('{:3d}:{:13s}'.format(cnt,word),end=' ')
        if print_cols == 3:
            print()
            print_cols = 0
        else:
            print_cols += 1
 
#def main():
file_str = input('What file: ')
file_obj = open(file_str)
my_dict = {}
get_words(file_obj,my_dict)
file_obj.close()
print('There were {:d} words in the file {:s}'.format(len(my_dict),file_str))
print_alphabetic(my_dict)
print_frequency(my_dict)
#return my_dict
    
