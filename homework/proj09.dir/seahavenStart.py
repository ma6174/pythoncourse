import cardsBasic

def setup():
    """
    paramaters: None
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 10 lists, the dealt cards)
    """
    foundation = None # place holder
    tableau = None # place holder
    cell = None # place holder
    
    return foundation,tableau,cell


def move_to_foundation(tableau,foundation,t_col,f_col):
    '''
    parameters: a tableau, a foundation, column of tableau, column of foundation
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    pass


def move_to_cell(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    pass

def move_to_tableau(tableau,foundation,t_col,f_col):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    '''
    pass
        

def is_winner(foundation):
    '''
    parameters: a foundation
    return: Boolean
    '''
    pass


def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    pass
        
def print_game(foundation, tableau,cell):
    """
    parameters: a tableau, a foundation and a cell
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  
        b) print foundation ( can print the top card only)
        c) print cells

    """
    cell_found = '''
      F1      F2      C1      C2      C3      C4      F3      F4
'''
    print(cell_found)

    row = ''
    for stack in foundation[0:2]:
        try:
            row += '%8s' % stack[-1]
        except IndexError:
            row += '%8s' % ''
            
    for c in cell:
        
        try:
            row += '%8s' % c[0]
        except IndexError:
            row += '%8s' % ''
            
    row = row+ ' '
    for stack in foundation[2:]:
        try:
            row += '%8s' % stack[-1]
        except IndexError:
            row += '%8s' % ''

    print (row)
    print ('----------')


    
    print ("Tableau")
    row = ''
    for i in range(len(tableau)):
        row += '%8s' % (i + 1)
    print (row)

    """find the length of the longest stack"""
    stack_length = []
    for stack in tableau:
        stack_length.append(len(stack))
    max_length = max(stack_length)

    for i in range(max_length):
        row = ''                    # remember to clear the row
        for stack in tableau:
            try:
                row += '%8s' % stack[i]
            except IndexError:
                row += '%8s' % ''
        print (row)
    print ('----------')

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    to_print ='''Rules of Seahaven Towers

    a. Only one card at a time can be moved.
    b. Foundation
        Each foundation holds only one suit and is built up from Ace to King.
        You can move a card to the foundation from a cell or the tableau.
        Once a card is on the foundation it cannot be moved off.
    c. Tableau 
        i. The card at the bottom of a column may be moved to an open cell,
           a foundation or another column of the tableau.
        ii. Moving a card to a tableau column follows these rules
            1. A card can only be moved to the bottom of a column
            2. When you move a card to a column in the tableau you can only
               build down by rank and by the same color. For example, you
               can move a Two of Hearts onto a Three of Hearts (the pile goes
               down by rank, and same color)
        iii. Empty columns may be filled only by a King with any color.
    d. Cell
        i. One cell spot can only contain 1 card
        ii. The card may be moved to the tableau or the foundation.
'''
    print(to_print)

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    response ='''
    Responses are:
    --------------
         t2f T F   - move from Tableau T to Foundation F (T and F are ints)
	 t2c T C   - move from Tableau T to Cell C (T and C are ints)
	 t2t T1 T2 - move from Tableau T1 to Tableau T2 (T1 and T2 are ints)
	 c2t C T   - move from Cell C to Tableau T (C and T are ints)
	 c2f C F   - move from Cell C to Foundation F (C and F are ints)
	 'h' for help
	 'q' to quit
         '''
    print (response)
         

    

    
def play():
    ''' 
    main program. Does error checking on the user input. 
    '''
    print_rules()
    foundation, tableau, cell = setup() 
       
    show_help()
    while True:
        # Uncomment this next line. It is commented out because setup doesn't do anything so printing doesn't work.
        # print_game(foundation, tableau, cell)
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split()
        if len(response_list) > 0:
            r = response_list[0]
            if r == 't2f':
                pass # you implement                          
            elif r == 't2t':
                pass # you implement                          
            elif r == 't2c':
                pass # you implement                          
            elif r == 'c2t':
                pass # you implement                          
            elif r == 'c2f':
                pass # you implement                          
            elif r == 'q':
                break
            elif r == 'h':
                show_help()
            else:
                print('Unknown command:',r)
        else:
            print("Unknown Command:",response)
    print('Thanks for playing')

play()


        
    

