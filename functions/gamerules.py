class gameplay:
    def __init__(self):
        self.player_card_score = 0
        self.house_card_score = 0
        self.player_drawn_cards = []
        self.house_drawn_cards =[]

    def start_new_game(self):
        self.player_card_score = 0
        self.house_card_score = 0
        self.player_drawn_cards = []
        self.house_drawn_cards =[]

    def get_person(self, number):
        if number == 1:
            return [self.player_card_score, self.player_drawn_cards]
        else:
            return [self.house_card_score, self.house_drawn_cards]

    def player_get_card_score(self):
        return self.player_card_score

    def player_add_card_to_drawn_cards(self, card_drawn):
        self.player_drawn_cards.append(card_drawn)

    def house_get_card_score(self):
        return self.house_card_score
    
    def house_add_card_to_drawn_cards(self, card_drawn):
        self.house_drawn_cards.append(card_drawn)

    # Check card score is used for troubleshooting purposes, but can be used for the game as well.
    def check_card_score(self, person, card):
        card_score = self.get_person(person)[0]
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
    def count_cards(self,person):
        drawn_cards = self.get_person(person)
        local_score = 0
        isAce = 0
        
        # Checks the drawn cards
        for card in drawn_cards[1]:
            card_value = card[0]
            # This helped me here: https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
            if isinstance(card_value, str):
                if 'A' == card_value:   # If the card is an Ace
                    isAce+=1
                else:                   # If the card is a King, Queen, or Jack
                    local_score+=10
            else:
                local_score+=card_value

        # If the score is less or at 10, aces should be 11. If more than 10, aces should be 1 
        if ((11*isAce) + local_score) <= 21:
            local_score+=(11*isAce)
        else:
            local_score+=isAce

        # Since local score is the best score, it is now the game's score
        drawn_cards[0] = local_score
             
    # Checks the player's score to see if they should be still playing.
    def check_if_still_playing(self, person):
        person_to_check = self.get_person(person)
        return (person_to_check[0] < 21)
    

