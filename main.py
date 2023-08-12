from functions.deck import deck
from functions.gamerules import gameplay
from functions.scoreboard import scorekeeper
from time import sleep

card_deck = deck()
score = scorekeeper()
gameplay = gameplay(score)

dealtime = 2



def game():
    print("(You walk up to the table confidently with 100 points in your pocket and take a seat at a blackjack table)")
    print("(The man looks at you)")
    print("Hi! Welcome to Blackjack!\n\n")

    leave = False

    while (score.get_player_score() > 0) and (leave is False):
        # Bidding
        leave = bid()
        if(leave):
            print("You leave the table with " + str(score.get_player_score()))
        else:
            # Gameplay
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
    
    if (score.get_player_score() <= 0):
        print("Oh, it looks like you are out of funds... Boys! Get this person out of here!")
        sleep(dealtime)
        print("You get up and try to run but the 2 large people come up to you, grab you, and push you outside.")
        sleep(dealtime)
        print("Well, there\'s no way home... So I guess I will sleep here...")
        sleep(dealtime)
        print("You fell asleep on the concrete outside of the casino...")
        sleep(dealtime)
        print("Thanks for playing!")
    else:
        print("You then see the doors open by two men holding the door for you.")
        sleep(dealtime)
        print("You pass the two men holding the door with a smile.")
        sleep(dealtime)
        print("You then look in your pockets and see that your winnings.")
        sleep(dealtime)
        print("\"Ahh, " + str(score.get_player_score()) + " points... \" You say to yourself")
        sleep(dealtime)
        print("What will I do with these points? Buy a fancy car? A house? Or charity?")
        sleep(dealtime)
        print("\"Oh I don't know, let\'s just go home and enjoy the evening.\"")
        sleep(dealtime)
        print("You get into your car and then start to drive home... The end.")
        sleep(dealtime)
        for i in range(5):
            print(".", end='')
            sleep(dealtime/2)
        print(" or is it???")
        sleep(dealtime*2)
        print("\nThanks for playing!")



def bid():
    print("What is your bid? Bid 0 to leave table.\n")
    sleep(dealtime/2)
    print("Current points: " + str(score.get_player_score()))
    has_bid = False
    while(not has_bid):
        try:
            bid = int(input("Bid: "))
            if (bid > score.get_player_score()):
                print("...\nI think that you are short in funds... Could you make a bid that you can afford?")
            elif (bid < 0):
                print("...\nI don\'t let people play for free around here. You\'re going to need to make a bid")
            elif (bid == 0):
                print("You get up from the table")
                has_bid = True
                escape = True
            else:
                print("Alright, here we go!")
                score.set_bet(bid)
                has_bid = True
                escape = False
        except KeyboardInterrupt:
            has_bid = True
            escape = True
        except:
            print("Could you repeat that in gambling terms this time?\n")
    sleep(dealtime/2)
    return escape



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