# rje: this is not a good example
# Demonstrate Break and Continue
while True:
    s = input('Enter a string longer than 3 ("quit" to end): ')
    if s == 'quit':
        break
    if len(s) < 4:
        print("Too short!")
        continue   # try again
    print('Input is of sufficient length')
    print('You entered: ', s)

print('Thanks for playing')
