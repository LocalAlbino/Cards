import random
import unicodedata

# Define constants for card suits and value.
SUIT = [
    "Spades",
    "Hearts",
    "Diamonds",
    "Clubs",
]
VALUE = [
    "Ace",
    "Teo",
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
        self.face = unicodedata.lookup("Playing Card " + self.value)
        self.isDiscarded = False
        
    def setCard(self, suit, value):
        self.suit = suit
        self.value = value
        if value != BACK:
            self.face = unicodedata.lookup("Playing Card " + value + " of " + suit)
        else:
            self.face = unicodedata.lookup("Playing Card " + value)
    
    def discard(self):
        self.isDiscarded = True
    
    def print(self):
        print(self.face)
        
def initializeDeck(deck):
    n = 0
    for i in SUIT:
        for j in VALUE:
            deck[n
            

# Declare deck as a list of 52 cards.
deck = [Card()] * 52

initializeDeck(deck)
