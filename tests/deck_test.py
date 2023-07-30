import sys
sys.path.insert(1,'/workspaces/python-blackjack/functions/')   
import deck

card_deck = deck.deck()
card_deck.make_deck()
print(card_deck.show_play_deck())

drawn_card = card_deck.draw()
print(str(drawn_card[0]) + " of " + drawn_card[1])

print(card_deck.show_play_deck())