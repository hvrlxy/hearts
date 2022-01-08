# This is a program that aims to simulate a game of hearts, a famous family cards game
# The objective is to create a model that can outplayed human player

#import libraries and codes
from hearts import Hearts

# First, we need an environment of a game of hearts
heart = Hearts(num_player=4, target_score=100)

# Model 1: control model
# start a game of hearts with 4 random machine players
# winner = heart.new_game()

# played the machine against each other for 100 times to see the result
winning = [0 for i in range(4)]
for i in range(100):
    winner = heart.new_game()
    winning[winner] += 1

print(winning)
