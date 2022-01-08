from functools import total_ordering

@total_ordering
class Card:
    is_played = False
    ordering = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,
                "J":11, "Q": 12, "K": 13, "A": 14}

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def same_suit(self, other):
        return self.suit == other.suit

    def __lt__(self, other):
        return self.ordering[self.value] < self.ordering[other.value]

    def __eq__(self, other):
        return self.ordering[self.value] == self.ordering[other.value]

    def is_heart(self):
        return self.suit == 'heart'

    def is_Qspade(self):
        return self.suit == 'spade' and self.value == 'Q'

    def card_score(self):
        if self.is_Qspade():
            return 13
        elif self.is_heart():
            return 1
        else:
            return 0

    def __str__(self):
        return "("+self.suit+', '+self.value+")"

    def __repr__(self):
        return "("+self.suit+', '+self.value+")"

# test
# card1 = Card('heart', 'A')
# card2 = Card('heart', '10')
#
# print(card1)
