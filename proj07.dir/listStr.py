word = input("Please enter a one-word string: ")

# STRING TO LIST:
# list() function iterates through the string, 
# making each letter a string element of the list.
letters_list = list(word)
print("A list of the word's letters is:",letters_list)

# LIST TO STRING:
# join() function assembles letters of a list,
# with the lead string between each letter.
# If that lead string is the empty string, 
# it just makes the list of letters a single string.
word_str=''.join(letters_list)
print("That list reassembled as a string is:",word_str)
word_str = ','.join(letters_list)
print("Now with commas", word_str)
