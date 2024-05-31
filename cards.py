import random
import unicodedata

# Define constants for card suits and value.
SUIT = [
    "Spades",
    "Hearts",
    "Diamonds",
    "Clubs"
]
VALUE = [
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King"
]

class Card:
    # Blank card by default
    def __init__(self):
        self.suit = SUIT[0]
        self.value = VALUE[0]
        self.face = unicodedata.lookup("Playing Card Back")
        self.isDiscarded = False
        
    def setCard(self, suit, value):
        self.suit = suit
        self.value = value
        self.face = unicodedata.lookup("Playing Card " + value + " of " + suit)

    def discard(self):
        self.isDiscarded = True
    
    def print(self):
        print(self.face)
        
def initializeDeck(deck):
    for i in range(52):
        deck.append(Card())

    # Variable for current card being updated, Loops update the entire deck.
    card = 0
    for i in range(len(SUIT)):
        for j in range(len(VALUE)):
            deck[card].setCard(SUIT[i], VALUE[j])
            card += 1

# Declare deck as a list of 52 cards.
deck = []
initializeDeck(deck)
# TEST: Print all elements in deck to see if it displays correctly.
for i in range(len(deck)):
    deck[i].print()
