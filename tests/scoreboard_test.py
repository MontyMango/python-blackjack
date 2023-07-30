import sys
sys.path.insert(1,'/workspaces/python-blackjack/functions/')   
from scoreboard import scoreboard

score = scoreboard()

print(score.get_player_score())
print("You will bid 10 scores")
score.set_bet(10)
print("You won!")
score.win()
print("Your current score: " + str(score.get_player_score()))

print("\n")

print("Oh, you want to bid everything? Okay....")
score.set_bet(110)
print("You lose everything!")
score.lose()
print("Your current score: " + str(score.get_player_score()))
print("Get out of here broke boy!")
