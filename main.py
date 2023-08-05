from functions.deck import deck
from functions.gamerules import gameplay
from functions.scoreboard import scorekeeper
from time import sleep

card_deck = deck()
score = scorekeeper()
gameplay = gameplay(score)

dealtime = 2



def game():
    while score.get_player_score() > 0:
        print("Let's begin!\n\n")
        gameplay.start_new_game()
        card_deck.make_deck()

        print("Here are your two cards")
        sleep(dealtime)

        # Draw two cards for each the player and house
        for i in range(2):
            card = card_deck.draw()
            gameplay.player_add_card_to_drawn_cards(card)
            card = card_deck.draw()
            gameplay.house_add_card_to_drawn_cards(card)
    
        print("*You flip your cards*")
        sleep(dealtime)
        print("Your cards: " + str(gameplay.player_drawn_cards))
        sleep(dealtime/2)
        print("You total score: " + str(gameplay.player_get_card_score()))
        sleep(dealtime/2)

        player_play()
        house_play()
        gameplay.win_check()
        print("\n\n\n\n\n")



def player_play():
    move = 0
    not_fold = True
    while(gameplay.player_status() and not_fold):
        print("\n\n\nYour Score Now: " + str(gameplay.player_get_card_score()) + "\n1. Draw\n2. Stay")
        try:
            play = int(input("Choice > "))
            if play == 1:       # Draw
                print("You flip another card...")
                card = card_deck.draw()
                gameplay.player_add_card_to_drawn_cards(card)
                print("You drew a " + str(card[0]) + " of " + str(card[1]) + "!")
                print("Your new score: " + str(gameplay.player_get_card_score()))
                move += 1

            elif play == 2:     # Stay
                print("You are staying at " + str(gameplay.player_get_card_score()))
                not_fold = False

            else:
                print("Please pick another number!")

            # Double down will be available later
        except:
            print("Uhh that\'s not a number! Try again!")
        sleep(dealtime/2)

# Since class deck is only accessed here.
def house_play():
    print("House will now play")    # This is used for debugging purpose
    sleep(dealtime) 
    print("\n*House flips their cards*")
    sleep(dealtime/2)
    print("House\'s cards: " + str(gameplay.house_drawn_cards))
    sleep(dealtime/2)
    print("House\'s score: " + str(gameplay.house_get_card_score()))

    # Debugging purpose: to see if methods worked for bot
    # print("-= Debug: Is house <= 17?: " + str(gameplay.house_get_card_score() <= 17) + " | Is player beating house?: " + str(gameplay.is_player_beating_house()) + " =-")
    
    # House stands on 17
    while((gameplay.house_get_card_score() <= 17)): # and (gameplay.is_player_beating_house()) # <-- Since house stands on 17, this will be added later
        
        # Debugging purpose: to see if methods worked for bot
        # print("-= Debug: Is house <= 17?: " + str(gameplay.house_get_card_score() <= 17) + " | Is player beating house?: " + str(gameplay.is_player_beating_house()) + " =-")
        
        card = card_deck.draw()
        print("House drew a " + str(card[0]) + " of " + str(card[1]))
        sleep(dealtime/2)
        gameplay.house_add_card_to_drawn_cards(card)
        print("House score: " + str(gameplay.house_get_card_score()))
        sleep(dealtime/2)

        


if __name__ == '__main__':
    game()