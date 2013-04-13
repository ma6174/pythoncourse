import cardsBasic
''' The basic process is this:
    1) You create a Deck instance, which is filled (automatically) with 52 Card instances
    2) You can deal those cards out of the deck into hands, each hand a list of cards
    3) You then manipulate cards as you add/remove them from a hand
'''
my_deck = cardsBasic.Deck()
print("======messy print a deck=====")
print(my_deck)

print("======pretty print a deck=====")
my_deck.pretty_print()

my_deck.shuffle()
print("======shuffled deck=====")
my_deck.pretty_print()

a_card = my_deck.deal()
print("Dealt card is:",a_card)
print('How many cards left:',my_deck.cards_count())

print("Is the deck empty?",my_deck.is_empty())

# deal some hands and print
hand1_list=[]
hand2_list=[]
for i in range(5):
    hand1_list.append(my_deck.deal())
    hand2_list.append(my_deck.deal())
                      
print("\nHand 1:", hand1_list)
print("Hand 2:", hand2_list)
print()

# take the last card dealt out of each hand
last_card_hand1 = hand1_list.pop()
last_card_hand2 = hand2_list.pop()
print("Hand1 threw down",last_card_hand1, ", Hand2 threw down", last_card_hand2)
print("Hands are now:",hand1_list, hand2_list)

# check the compares
if last_card_hand1.equal_rank(last_card_hand2):
    print(last_card_hand1, last_card_hand2, "of equal rank")
elif last_card_hand1.get_rank() > last_card_hand2.get_rank():
    print(last_card_hand1, "of higher rank than",last_card_hand2)
else:
    print(last_card_hand2, "of higher rank than",last_card_hand1)

if last_card_hand1.equal_value(last_card_hand2):
    print(last_card_hand1, last_card_hand2, "of equal value")
elif last_card_hand1.get_value() > last_card_hand2.get_value():
    print(last_card_hand1, "of higher value than",last_card_hand2)
else:
    print(last_card_hand2, "of higher value than",last_card_hand1)

if last_card_hand1.equal_suit(last_card_hand2):
    print(last_card_hand1,'of equal suit with',last_card_hand2)
else:
    print(last_card_hand1,'of different suit than',last_card_hand2)

# a foundation, a list of lists. 4 columns in this example
foundation_list = [[],[],[],[]]
column = 0
while not my_deck.is_empty():
    foundation_list[column].append(my_deck.deal())
    column += 1
    if column % 4 == 0:
        column = 0
for i in range(4):
    print("foundation",i,foundation_list[i])


