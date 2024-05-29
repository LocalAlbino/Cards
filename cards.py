import random

# Define constants for card suits and values.
SPADES = "A"
HEARTS = "B"
DIAMONDS = "C"
CLUBS = "D"

BLANK = "0"
ACE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"
SEVEN = "7"
EIGHT = "8"
NINE = "9"
TEN = "A"
JACK = "B"
QUEEN = "D"
KING = "E"

UNICODE = "U0001F0"

class Card:
    # Blank card by default.
    suit = SPADES
    value = BLANK
    face = UNICODE + suit + value
    isDiscarded = False
    
    def setCard(self, suit, value, face):
        self.suit = suit
        self.value = value
        face = UNICODE + suit + value
        
    def discard(self):
        self.isDiscarded = True
    
    def print(self):
        print(self.face)
        
# Declare deck as a list of 52 cards.
deck = [Card()] * 52

# Initialize deck.
for i in 52:
    