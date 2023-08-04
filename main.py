from functions.deck import deck
from functions.gamerules import gameplay
from functions.scoreboard import scorekeeper
import time

card_deck = deck()
score = scorekeeper()
gameplay = gameplay(score)

def game():
    while score.get_player_score > 0:
        print("Let's begin!\n\n")
        card_deck.make_deck()

        print("Here are your two cards")
        time.sleep(1)

        # Draw two cards for each the player and house
        for i in range(2):
            card = card_deck.draw
            gameplay.player_add_card_to_drawn_cards(card)
            card = card_deck.draw
            gameplay.house_add_card_to_drawn_cards(card)
    
        print("You flip your cards")
        print("Your cards: " + str(gameplay.player_drawn_cards))
        print("You total score: " + str(gameplay.player_card_score()))

        player_play()
        house_play()
        gameplay.win_check()








def player_play():
    move = 0
    fold = False
    while(gameplay.can_player_still_play() or fold):
        print("\n\n\nYour Score Now: " + str(gameplay.player_card_score()) + "\n1. Draw\n2. Stay")
        play = input("Choice > ")
        if play == 1:       # Draw
            print("You flip another card...")

            card = card_deck.draw()
            gameplay.player_add_card_to_drawn_cards(card)

            print("You drew a " + str(card[0]) + " of " + str(card[1]) + "!")
            print("Your new score: " + str(gameplay.house_get_card_score))
            move += 1

        elif play == 2:     # Stay
            print("You stay at " + str(gameplay.player_get_card_score()))
            fold = True

        # Double down will be available later

        else:
            print("Command not understood! Try again!")

# Since class deck is only accessed here.
def house_play():
    print("House will now play")    # This is used for debugging purpose 
    print("\n*House flips their cards*")
    print("House cards: " + str(gameplay.house_drawn_cards))

    # House stands on 17
    while((gameplay.house_get_card_score <= 17) or (gameplay.is_house_beating_player)):
        card = card_deck.draw()


if __name__ == '__main__':
    game()