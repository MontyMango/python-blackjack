class scoreboard:
    def __init__(self):
        self.player_score = 100     # The player starts out with 100 score
        self.bet = 0

    # Sets the bet 
    def set_bet(self, bid):
        self.bet = bid
        self.player_score-=self.bet
    
    def get_player_score(self):
        return self.player_score
    
    def get_bet(self):
        return self.bet
    
    # Winning the game in blackjack multiplies your bet by 2, and adds it to your score.
    def win(self):
        self.player_score = self.player_score + (self.bet * 2)
        
    # Since set_bet does all the hard work, lose is basically useless right now
    def lose(self):
        pass

    # If there is a tie or both bust. A refund is initated.
    def refund(self):
        self.player_score+=self.bet