# This helped here: https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
import sys
sys.path.insert(1,'/workspaces/python-blackjack/functions/')   
from gamerules import gameplay

game = gameplay()

cards_to_try = [ ['A', 'Spades'], [10, 'Spades'],
                 [2, 'Hearts'], ['K', 'Clubs'] ]

# PLAYER
for card in cards_to_try:
    game.player_add_card_to_drawn_cards(card)
    print("Current Card Score: " + str(game.check_card_score(0, card)))
    game.count_cards(0)
    print("Total Player Card Score: " + str(game.player_get_card_score()))
    print("\n")

# HOUSE
for card in cards_to_try:
    game.house_add_card_to_drawn_cards(card)
    print("Current Card Score: " + str(game.check_card_score(1, card)))
    game.count_cards(1)
    print("Total House Card Score: " + str(game.house_get_card_score()))
    print("\n")