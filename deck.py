from cards import Card
import random as rd

class Deck:
    suits = ['heart', 'spade', 'diamond', 'club']
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                "J", "Q", "K", "A"]
    def __init__(self):
        self.cards_list = []
        for suit in self.suits:
            for value in self.values:
                self.cards_list.append(Card(suit, value))

    def shuffle_deck(self):
        rd.shuffle(self.cards_list)

    def deal_cards(self, num_player=4):
        player_cards = [[] for i in range(num_player)]

        while len(self.cards_list) > 0:
            for i in range(num_player):
                player_cards[i].append(self.cards_list.pop())

        return player_cards

    def print_deck(self):
        print(self.cards_list)
        print(len(self.cards_list))

#test
# deck = Deck()
# deck.shuffle_deck()
# deck.print_deck()
# print(deck.deal_cards())
