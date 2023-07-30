from functions.gamerules import gameplay

game = gameplay()

cards_to_try = [ ['A', 'Spades'], [10, 'Spades'],
                 [2, 'Hearts'], ['K', 'Clubs'] ]

for card in cards_to_try:
    game.add_card_to_drawn_cards(card)
    print("Current Card Score: " + str(game.check_card_score(card)))
    game.count_cards()
    print("Total Card Score: " + str(game.get_card_score()))
    print("\n")