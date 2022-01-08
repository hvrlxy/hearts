from cards import Card
import random as rd

class Player:
    suits = ['heart', 'spade', 'diamond', 'club']
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        self.score = 0
        self.cards_received = []
        self.club = []
        self.heart = []
        self.diamond = []
        self.spade = []

    def get_cards(self, cards_list):
        self.cards = cards_list
        self.club = []
        self.heart = []
        self.diamond = []
        self.spade = []

    def pass_cards(self):
        rd.shuffle(self.cards)
        return [self.cards.pop() for i in range(3)]

    def receive(self, cards):
        self.cards.extend(cards)

    def reorganize(self):
        for card in self.cards:
            if card.suit == 'club':
                self.club.append(card)
            elif card.suit == 'heart':
                self.heart.append(card)
            elif card.suit == 'spade':
                self.spade.append(card)
            else:
                self.diamond.append(card)

    def score(self):
        total_score = 0
        for card in self.cards_received:
            total_score += card.card_score()
        self.score = total_score

    def is_first(self):
        for card in self.club:
            if card.value == '2':
                return True
        return False

    def get_suit(self, suit=None):
        card_suit = []
        if suit == 'heart':
            card_suit = self.heart
        elif suit == 'club':
            card_suit = self.club
        elif suit == 'spade':
            card_suit = self.spade
        elif suit == 'diamond':
            card_suit = self.diamond

        if len(card_suit) == 0:
            new_suit = rd.choice(self.suits)
            return self.get_suit(new_suit)
        return card_suit

    def play(self, suit):
        #return the card played
        if self.is_first():
            self.club.remove(Card('club', '2'))
            return Card('club', '2')

        card_suit = self.get_suit(suit)
        rd.shuffle(card_suit)
        return card_suit.pop()

    def is_empty(self):
        return len(self.heart) + len(self.spade) + len(self.club) + len(self.diamond) == 0

    def __str__(self):
        club_str = 'club: ' + str(self.club)
        heart_str = 'heart: ' + str(self.heart)
        diamond_str = 'diamond: ' + str(self.diamond)
        spade_str = 'spade: ' + str(self.spade)

        return club_str + '\n' + heart_str + '\n' + diamond_str + '\n' + spade_str


#test
# player1 = Player()
# cards = [Card('heart', 'A'), Card('heart', '6'), Card('heart', 'J'), Card('spade', '9'),
#          Card('heart', '2'), Card('heart', 'K'), Card('spade', '3'), Card('spade', '7'),
#          Card('club', '8'), Card('diamond', '7'), Card('club', '5'), Card('heart', '4'), Card('spade', 'J')]
# player1.get_cards(cards)
# player1.reorganize()
# while not (player1.is_empty()):
#     player1.play('heart')
#     print(player1)
#     print('\n')

