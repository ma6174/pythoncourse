import random    # required for shuffle method of Deck

class Card(object):
    ''' suit and rank are ints, and index into suit_list and rank_list
        value is different from rank: for example face cards are equal in value (all 10)
    '''
    # use these lists to map the ints of suit and rank to nice words.
    # the 'x' is a place holder so that index-2 maps to '2', etc.
    suit_list = ['x','c','d','h','s']
    rank_list = ['x', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K']

    def __init__(self, rank=0, suit=0):
        ''' rank and suit must be ints. Make sure they are in the correct range
            blank card has rank and suit set to 0
        '''
        if type(suit) == int and type(rank) == int:
            # only good indicies work
            if suit in range(1,5) and rank in range(1,15):
                self.__suit = suit
                self.__rank = rank
        else:
            self.__suit = 0
            self.__rank = 0

    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit

    def get_value(self):
        ''' face cards are 10, the rest are their rank/index values
            remember, aces are low
        '''
        # ternary expression:
        return self.__rank if self.__rank < 10 else 10

    def equal_suit(self, other):
        return self.__suit == other.__suit

    def equal_rank(self, other):
        return self.__rank == other.__rank

    def equal_value(self, other):
        return self.get_value() == other.get_value()

    def __str__(self):
        ''' allows you to print a card, just like any other data structure
        '''
        return "{:s}{:s}".format((self.rank_list)[self.__rank], (self.suit_list)[self.__suit])

    def __repr__(self):
        ''' if you print in the console, it also works with this
        '''
        return self.__str__()

class Deck(object):
    ''' deck of cards, as a list of card objects
        last card in the deck/list is top of deck
    '''
    def __init__(self):
        self.__deck=[Card(rank,suit) for rank in range(1,14) for suit in range(1,5)]

    def shuffle(self):
        random.shuffle(self.__deck)

    def deal(self):
        # ternary expression
        return self.__deck.pop() if len(self.__deck) else None

    def cards_count(self):
        return len(self.__deck)

    def is_empty(self):
        return len(self.__deck) == 0

    def __str__(self):
        ''' print a deck, but messy!
        '''
        return ','.join([str(card) for card in self.__deck])
            
    def __repr__(self):
        ''' messy print deck to console
        '''
        return self.__str__()

    def pretty_print(self, column_max=10):
        ''' column oriented printing of a deck
        '''
        for index,card in enumerate(self.__deck):
            if index%column_max == 0:
                print()
            else:
                print(' ',end='')
            print("{:3s}".format(card), end='')
        print()
        print()
