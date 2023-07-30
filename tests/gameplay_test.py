# This helped here: https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
import sys
sys.path.insert(1,'/workspaces/python-blackjack/functions/')   
from gamerules import gameplay

game = gameplay()

cards_to_try = [ ['A', 'Spades'], [10, 'Spades'],
                 [2, 'Hearts'], ['K', 'Clubs'] ]

for card in cards_to_try:
    game.player_add_card_to_drawn_cards(card)
    print("Current Card Score: " + str(game.check_card_score(card,0)))
    game.count_cards()
    print("Total Card Score: " + str(game.get_card_score()))
    print("\n")