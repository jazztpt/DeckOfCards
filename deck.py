import random
import itertools


SUITS = ["clubs", "hearts", "spades", "diamonds"]
RANKS = ['2','3','4','5','6','7','8','9','Ten','Jack','Queen','King','Ace']

class Deck(object):
    """
    Represents a standard deck of 52 cards (13 of each suit, no jokers).
    """

    def __init__(self):
        self.cards = []
        self._create_full_deck()

    def _create_full_deck(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append((rank,suit))
        print self

    def shuffle(self):
        self.cards = []
        self._create_full_deck()
        random.shuffle(self.cards)
        print "SHUFFLING CARDS:"
        print self

    def get_next_card(self):
        try:
            card = self.cards.pop()
            return card
        except IndexError:
            return "The deck is empty.  Try shuffling or re-initializing to start with a sorted deck."

    def __repr__(self):
        string = ""
        for card in self.cards:
            string = string + "{0} of {1} \n".format(card[0],card[1])
        return string