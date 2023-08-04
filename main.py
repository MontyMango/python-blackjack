from functions.deck import deck
from functions.gamerules import gameplay
from functions.scoreboard import scoreboard
import time

card_deck = deck()
score = scoreboard()
game = gameplay(score)

def game():
    print("Let's begin!\n\n")
    card_deck.make_deck()

    print("Here are your two cards")
    time.sleep(1)
    for i in range(2):
        card = card_deck.draw
        
        game.player_add_card_to_drawn_cards(card)


    

if __name__ == '__main__':
    game()