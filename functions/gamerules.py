class gameplay:
    def __init__(self, scoreboard_class):
        self.player_card_score = 0
        self.house_card_score = 0
        self.player_drawn_cards = []
        self.house_drawn_cards = []
        self.score = scoreboard_class

    def start_new_game(self):
        self.player_card_score = 0
        self.house_card_score = 0
        self.player_drawn_cards = []
        self.house_drawn_cards = []

    # get_person
    # 0 - Player
    # 1 - House
    def get_person_info(self, number):
        if number == 0:
            return [self.player_card_score, self.player_get_cards()]
        else:
            return [self.house_card_score, self.house_get_drawn_cards()]


    # Player Getters
    def player_get_card_score(self):
        return self.player_card_score
    
    def player_get_cards(self):
        return self.player_drawn_cards

    # Add to drawn cards and recount the cards
    def player_add_card_to_drawn_cards(self, card_drawn):
        self.player_drawn_cards.append(card_drawn)
        self.recount_card_score(0)


    # House Getters
    def house_get_card_score(self):
        return self.house_card_score
    
    def house_get_drawn_cards(self):
        return self.house_drawn_cards
    
    # Add to drawn cards and recount the cards
    def house_add_card_to_drawn_cards(self, card_drawn):
        self.house_drawn_cards.append(card_drawn)
        self.recount_card_score(1)



    # Check card score is used for troubleshooting purposes, but can be used for the game as well.
    def check_card_score(self, person, card):
        card_score = self.get_person_info(person)[0]     # Get the person's score
        if isinstance(card[0], str):
            if 'A' == card[0]:   # If the card is an Ace
                if (11 + card_score) <= 21:
                    return 11
                else:
                    return 1
            else:
                return 10         # If the card is a King, Queen, or Jack    
        else:
            return card[0]
        
    # count_cards is used to check if any change has happened to the score
    # due to Aces being either 1 or 11, the cards have to be checked everytime a card has been drawn
    # person_to_check: an int value that is used to check either house or the player
    def recount_card_score(self,person):
        # print(self.get_person_info(person))   # For debugging purposes: To see if person has score & a deck of cards
        drawn_cards = self.get_person_info(person)[1]
        # print(drawn_cards[0])                 # For debugging purposes: To see the drawn card
        local_score = 0
        isAce = 0
        
        # Checks the drawn cards
        for card in drawn_cards:
            card_value = card[0]
            # print("card value " + str(card_value))    # Debugging purpose: To see if card value is right
            # This helped me here: https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
            if isinstance(card_value, str):
                if 'A' == card_value:   # If the card is an Ace
                    isAce+=1
                else:                   # If the card is a King, Queen, or Jack
                    local_score+=10
            else:
                local_score+=card_value

            # print("Score: " + str(local_score))   # Debugging purpose: To see if card was added correctly

        # If the score is less or at 10, aces should be 11. If more than 10, aces should be 1 
        if ((11*isAce) + local_score) <= 21:
            local_score+=(11*isAce)
        else:
            local_score+=isAce

        # print("Final local Score: " + str(local_score))   # Debugging purpose: To see if Ace function worked
        
        # Since local score is the best score, it is now the game's score
        if person == 0:
            self.player_card_score = local_score
        else:
            self.house_card_score = local_score


    # Checks the player's score to see if they should be still playing.
    def player_status(self):
        if self.player_card_score < 21:     # This is usually the case
            return True
        # Added dialog
        elif self.player_card_score == 21:  # If 21 is hit, the game will stop for you
            print("21 nice! We will stop here!")
            return False 
        else:                               # If it is over 21, then it's a bust!
            print("oh no busted! :( ")
            return False

 
    def is_player_beating_house(self):
        return (self.player_card_score >= self.house_card_score)
    

    def win_check(self):
        # Added this for better code readability
        house_score = self.house_card_score
        player_score = self.player_card_score
        bet = str(self.score.get_bet())
        
        
        # Added these definitions in here for better readability and some plays end the same way.
        def player_won():
            print("You win! Here's " + (2 * bet) + " points!")
            print("You won " + bet + " (+" + bet + ")" + " points!")
            self.score.win()
        
        def house_won():
            print("You lose :(")
            print("You lost " + bet + " points")
            self.score.lose()

        def tie():
            print("It's a tie! You were refunded your points.")
            self.score.refund()

        def no_one_won():
            print("Both bust! Looks like no one won.")
            print("You recieved " + bet + " points back")
            self.score.refund()



        # If both house and player are both in play
        if (house_score <= 21) and (player_score <= 21):
            if house_score == player_score:     # If both scores are the same
                tie()
            elif house_score > player_score:    # If house wins
                house_won()
            else:                               # If player wins
                player_won()

        # If no one won!
        elif (house_score > 21) and (player_score > 21):
            no_one_won()
            
        # If house busts! Player wins!
        elif (house_score > 21):
            player_won()

        # If player busts. House wins.
        elif (player_score > 21):
            house_won()
        
        # If somehow, something odd happens, and the computer doesn't know what to do.
        else:
            print("Well, this is odd. What happened in that play? Let's just say it's a tie...")
            tie()