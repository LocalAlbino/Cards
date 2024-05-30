import random

# Define constants for card suits and unicode.
SPADES = "A"
HEARTS = "B"
DIAMONDS = "C"
CLUBS = "D"

# Define constants for card values in ASCII. Will be iterated in a loop
ACE = 47
JACK = 65

# Used to initialize cards to face down.
BLANK = "0"
UNICODE = "\U0001F0A0"

class Card:
    # Blank card by default.
    suit = SPADES
    value = BLANK
    face = UNICODE
    isDiscarded = False
    
    def setCard(self, suit, value):
        self.suit = suit
        self.value = value
        # FIXME: Convert list back to unicode to correctly display cards.
        face = list(self.face.encode())
        face[8] = suit
        face[9] = value

    def discard(self):
        self.isDiscarded = True
    
    def print(self):
        print(self.face)
        
def initializeDeck(start, end, suit, value, deck):
    for i in range(start, end):
        deck[i].setCard(suit, str(chr(value)))
        if value != 66:
            value += 1
        else:
            value += 2

# Declare deck as a list of 52 cards.
deck = [Card()] * 52

# Initialize each suit.
initializeDeck(0, 10, SPADES, ACE, deck)
initializeDeck(10, 13, SPADES, JACK, deck)
initializeDeck(13, 23, HEARTS, ACE, deck)
initializeDeck(23, 26, HEARTS, JACK, deck)
initializeDeck(26, 36, DIAMONDS, ACE, deck)
initializeDeck(36, 39, DIAMONDS, JACK, deck)
initializeDeck(39, 49, CLUBS, ACE, deck)
initializeDeck(49, 52, CLUBS, JACK, deck)

# TEST: Print card values to ensure they appear correctly.
for i in range(52):
    deck[i].print()
