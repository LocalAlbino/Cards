import random
import unicodedata

# Define constants for card suits and rank.
SUIT = [
    "Spades",
    "Hearts",
    "Diamonds",
    "Clubs"
]
RANK = [
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
# Declare number of discards per hand.
DISCARDS = 3

class Card:
    # Blank card by default
    def __init__(self):
        self.suit = SUIT[0]
        self.rank = RANK[0]
        self.face = unicodedata.lookup("Playing Card Back")
        self.isDiscarded = False
        self.isPlayed = False
        
    def setCard(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face = unicodedata.lookup("Playing Card " + rank + " of " + suit)

    def getDiscardState(self):
        return self.isDiscarded

    def getPlayState(self):
        return self.isPlayed

    def play(self):
        self.isPlayed = True

    def discard(self):
        self.isDiscarded = True
    
    def reset(self):
        self.isPlayed = False
        self.isDiscarded = False

    def print(self):
        print(self.face + " " + self.rank + " of " + self.suit)

# Initialize the deck to a standard 52 card deck.
def initializeDeck(deck):
    for i in range(52):
        deck.append(Card())

    # Variable for current card being updated, Loops update the entire deck.
    card = 0
    for suit in SUIT:
        for rank in RANK:
            deck[card].setCard(suit, rank)
            card += 1

# Draw cards from deck. Will draw as many as needed to fill hand to 5 cards.
def draw(deck, discards):
    played = 0
    for card in deck: # Check to see if 5 cards are already in play.
        if card.getPlayState() == True:
            played += 1
        if played >= 5:
            getInput()
            return

    for card in deck:
        if played < 5 and card.getDiscardState() == False and card.getPlayState() == False:
            card.print()
            card.play()
            played += 1
            if played >= 5:
                break
    getInput()
    return

def discard(deck, discards):
    if discards == 0:
        print("No more discards remaining.")
        getInput()
        return

    # Get input from user and loop while it is not a digit or "cancel".
    inp = input("Choose which cards to discard. \"1, 2, 3, 4, or 5\". (Multiple may be selected at once.)\nType \"cancel\" to cancel")
    for i in inp:
        if i.isdigit() == False and i.issapce() == False:
            break # Break from loop if current iteration is nt a digit or whitespace.
        elif i.isspace() == True: # Skip current iteration if whitespace.
            continue
        else:
            return # FIXME: Finish for loop.
        print("Try again.")
        inp = input("Choose which cards to discard. \"1, 2, 3, 4, or 5\". (Multiple may be selected at once.)\nType \"cancel\" to cancel")
 
    # Find cards that can be discarded.
    cards = []
    for card in deck:
        if card.getPlayState() == True:
            cards.append(card)
        if len(cards) == 5:
            break



def play():

def getInput(deck, discards):
    # Get user input.
    inp = input("Type \"play\", \"help\", \"discard\", or \"quit\".\n")
    inp = lower(inp) 

    # Loop until a valid choice is entered.
    while inp != "play" or inp != "help" or inp != "discard" or inp != "quit":
        print("Try again.")
        inp = input("Type \"play\", \"help\", \"discard\", or \"quit\".\n"")
        inp = lower(inp)

    match inp:
        case "play":
            play(deck)
        case "discard":
            discard(deck, discards)
        case "help":
            explain()
        case "quit":
            quit()

# Explain how each poker hand works.
def explain():
    print(
"""
Poker is played with a standard 52 card deck.
Each hand is played with 5 different cards.

Cards consisnt of four different suits:

🂡 Spades, 🂱 Hearts, 🃁 Diamonds, 🃑 Clubs.

Cards are ranked as follows: (from worst to best)

🂢 Two, 🂣 Three, 🂤 Four, 🂥 Five, 🂦 Six, 🂧 Seven, 
🂨 Eight, 🂩 Nine, 🂪 Ten, 🂫 Jack, 🂭 Quuen, 🂮 King, 🂡 Ace.

There are 9 types of hand you can have in poker;
they are: (from best to worst)

Straight Flush: (Five cards of the same suit played in ascending order.)
🂱 Ace of Hearts
🂾 King of Hearts    NOTE: This specific hand is also known as a royal flush.
🂽 Queen of Hearts         it is the best hand playable in poker.
🂻 Jack of Hearts
🂺 Ten of Hearts

Four of a Kind: (Four cards of the same rank)
🂡 Ace of Spades
🂱 Ace of Hearts
🃁 Ace of Diamonds
🃑 Ace of Clubs
🃆 Six of Diamonds

Full House: (A pair of cards with matching rank
            plus three cards of another matching rank)
🃂 Two of Diamonds
🃒 Two of Clubs
🂢 Two of Spades
🂻 Jack of Hearts
🃋 Jack of Diamonds

Flush: (Five cards of the same suit)
🃕 Five of Clubs
🃓 Three of Clubs
🃝 Queen of Clubs
🃚 Ten of Clubs
🃒 Two of Clubs

Straight: (Five cards of ascending order)
🃃 Three of Diamonds
🃔 Four of Clubs     NOTE: An 🂡 Ace can either be played
🂥 Five of Spades          before a 🂢 Two, or after a 🂮 King.
🂦 Six of Spades
🂷 Seven of Hearts

Three of a Kind: (Three cards of matching rank)
🂮 King of Spades
🃞 King of Clubs
🃎 King of Diamonds
🂽 Queen of Hearts
🃒 Two of Clubs

Two Pair: (Two pairs of cards with matching ranks)
🂢 Two of Spades
🃒 Two of Clubs
🂵 Five of Hearts
🃕 Five of Clubs
🂩 Nine of Spades

Pair: (A pair of cards with matching ranks)
🃘 Eight of Clubs
🂨 Eight of Spades
🃞 King of Clubs
🂷 Seven of Hearts
🂢 Two of Spades

High Card: (No cards of matching rank or suit.
            The highest ranked card will be scored.)
🂡 Ace of Spades
🂳 Three of Hearts
🃅 Five of Diamonds
🂪 Ten of Spades
🂾 King of Hearts

In order to try and make the best possible hand, 3 discards may be used.
You may discard up to 5 cards per discard. For example:

Given this hand. Type "discard" and then type
"1 2 3 4 5" in the next prompt to discard each card in the hand.
🂡 Ace of Spades     #1
🂳 Three of Hearts   #2
🃅 Five of Diamonds  #3
🂪 Ten of Spades     #4
🂾 King of Hearts    #5
"""
        )
    getInput(deck, discards)

discards = DISCARDS
deck = []
initializeDeck(deck)
random.shuffle(deck)

getInput(deck, discards)
