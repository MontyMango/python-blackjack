class scorekeeper:
    def __init__(self):
        self.player_score = 100     # The player starts out with 100 score
        self.bet = 0

    # GETTERS
    def get_player_score(self):
        return self.player_score
    
    def get_bet(self):
        return self.bet

    # SETTERS 
    def set_bet(self, bid):
        # Error correcting (Even though it is done all in the main application)
        if(bid <= self.player_score and bid > 0):
            self.bet = bid
            self.player_score-=self.bet
            return True
        elif(bid < 0):
            print('Your bid cannot be processed due to bidding a negative balance! STOP TRYING TO BE CLEVER AND BID WITH YOUR OWN MONEY!!!')
            return False
        else:
            print('Your bid cannot be processed due to your bid being larger than your player score. ', 'Player score: ', self.player_score, 'Bid: ', bid)
            return False
    
    
    # EVENT CONDITIONS
    # Winning the game in blackjack multiplies your bet by 2, and adds it to your score.
    def win(self):
        if(self.bet != 0):
            self.player_score = self.player_score + (self.bet * 2)
            self.bet = 0
            return True
        else:
            return False
        
    # Since set_bet does all the hard work, lose is basically useless right now
    def lose(self):
        if(self.bet != 0):
            self.bet = 0
            return True
        else:
            return False

    # If there is a tie or both bust. A refund is initated.
    def refund(self):
        if(self.bet != 0):
            self.player_score+=self.bet
            return True
        else:
            print("There is no active bet!")
            return False