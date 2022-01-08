from deck import Deck
from cards import Card
from player import Player
import pandas as pd
from IPython.display import display

class Hearts:
    def __init__(self, num_player=4, target_score=100):
        self.num_player = num_player
        self.target_score = target_score

        self.players = [Player() for i in range(num_player)]
        self.deck = Deck()
        self.score_board = [0 for i in range(num_player)]
        # self.set_up()

    def set_up(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        deals = self.deck.deal_cards()

        for i in range(self.num_player):
            self.players[i].get_cards(deals[i])

    def passing_cards(self, rotation: int):
        passed_cards = [player.pass_cards() for player in self.players]

        for i in range(self.num_player):
            self.players[i].receive(passed_cards[(i+rotation) % self.num_player])

    def find_first(self):
        #find the index of the player who leads the first trick
        for i in range(self.num_player):
            if self.players[i].is_first():
                return i

    def compare_cards(self, suit, cards_played):
        highest_card = None
        winning_index = -1
        for i in range(len(cards_played)):
            if cards_played[i].suit == suit:
                if highest_card is None:
                    highest_card = cards_played[i]
                    winning_index = i
                elif cards_played[i] > highest_card:
                    highest_card = cards_played[i]
                    winning_index = i

        return winning_index

    def trick(self, first=None):
        suit = None
        if first is None:
            first = self.find_first()
            suit = 'club'

        cards_played = []

        for i in range(self.num_player):
            card = self.players[(i + first) % self.num_player].play(suit)
            cards_played.append(card)
            if i == 0:
                suit = card.suit

        winning_index = self.compare_cards(suit, cards_played)
        self.players[winning_index].cards_received.extend(cards_played)

        return cards_played, winning_index

    def print_trick(self, cards_played, winning_index, score):
        for i in range(self.num_player):
            print('Player', i + 1, ':', cards_played[i])

        print('Player', winning_index + 1, 'wins the trick and receives', score, 'points.')

    def trick_scores(self, cards_played):
        total_score = 0
        for card in cards_played:
            total_score += card.card_score()
        return total_score

    def hearts_round(self, rotation):
        round_score = [0 for i in range(self.num_player)]

        self.set_up()
        self.passing_cards(rotation)
        leader = self.find_first()

        for i in range(self.num_player):
            self.players[i].reorganize()

        while not self.players[0].is_empty():
            cards_played, winning_index = self.trick(leader)
            leader = winning_index

            score = self.trick_scores(cards_played)
            self.print_trick(cards_played, winning_index, score)
            round_score[winning_index] += score

        shooting_the_moon = None

        #check for shooting the moon
        for i in range(self.num_player):
            if round_score[i] == 26:
                shooting_the_moon = i

        if shooting_the_moon is not None:
            for i in range(self.num_player):
                round_score[i] = 26
            round_score[shooting_the_moon] = 0

        return round_score, shooting_the_moon

    def print_round(self, round_score, total_score, shooting_the_moon):
        round_df = pd.DataFrame(columns=['Player', 'Round Score', 'Total Score'])
        for i in range(self.num_player):
            round_df.loc[len(round_df.index)] = ['Player'+str(i+1), round_score[i], total_score[i]]
        round_df = round_df.sort_values(ascending=True, by=['Total Score'])
        display(round_df)
        if shooting_the_moon is not None:
            print('Player', shooting_the_moon+1, 'shoots the moon!')

    def check_finish(self, total_score) -> bool:
        for i in range(self.num_player):
            if total_score[i] >= self.target_score:
                return True
        return False

    def print_game(self, total_score):
        game_df = pd.DataFrame(columns=['Player', 'Total Score'])
        for i in range(self.num_player):
            game_df.loc[len(game_df.index)] = ['Player'+str(i+1), total_score[i]]
        game_df = game_df.sort_values(ascending= True, by=['Total Score'])
        display(game_df)

        print(game_df['Player'].to_list()[0], 'wins the game!')
        return game_df['Player'].to_list()[0]

    def new_game(self):
        total_score = [0 for i in range(self.num_player)]

        rotation = 1
        while not self.check_finish(total_score):
            round_score, shooting_the_moon = self.hearts_round(rotation)
            for i in range(self.num_player):
                total_score[i] += round_score[i]
            self.print_round(round_score, total_score, shooting_the_moon)
            print('\n')
            rotation = (rotation + 1) % self.num_player
        winner = self.print_game(total_score)

        winner = int(winner[-1]) - 1
        return winner

