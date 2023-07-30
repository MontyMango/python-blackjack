from functions.gamerules import gameplay

game = gameplay()

drawn_card = ['A','Spades']
game.add_card_to_drawn_cards(drawn_card)
game.count_cards()
# 11
drawn_card = ['10','Spades']
game.add_card_to_drawn_cards(drawn_card)
game.count_cards()
# 2
print(game.get_card_score())

# There is something wrong with the calcuations!