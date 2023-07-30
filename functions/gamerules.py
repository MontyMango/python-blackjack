class gameplay:
    def __init__(self):
        self.card_score = 0
        self.drawn_cards = []

    def start_new_game(self):
        self.card_score = 0
        self.drawn_cards = []

    def get_card_score(self):
        return self.card_score

    def add_card_to_drawn_cards(self, card_drawn):
        self.drawn_cards.append(card_drawn)

    # Check card score is used for troubleshooting purposes
    def check_card_score(self, card):
        if isinstance(card[0], str):
            if 'A' == card[0]:   # If the card is an Ace
                if (11 + self.card_score) <= 21: return 11
                else: return 1
            else: return 10         # If the card is a King, Queen, or Jack    
        else: return card[0]
        
    # count_cards is used to check if any change has happened to the score
    # due to Aces being either 1 or 11, the cards have to be checked everytime a card has been drawn
    def count_cards(self):
        local_score = 0
        isAce = 0
        
        # Checks the drawn cards
        for card in self.drawn_cards:
            card_value = card[0]
            # This helped me here: https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
            # If the card isn't a number, 
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
        self.card_score = local_score
        
             
    # Checks the player's score to see if they should be still playing.
    def check_if_still_playing(self):
        if self.card_score < 21:
            return True
        else:
            return False
        
    # Checks to see if the player has a full house
    def full_house_check(self):
        if self.card_score == 21: 
            return True
        else: 
            return False
        
