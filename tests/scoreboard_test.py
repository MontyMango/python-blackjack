# scoreboard_test.py: Tests the scoreboard
import sys
import os
import pytest
# Used GitHub Co-Pilot to help me out with getting the functions path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))
from scoreboard import scorekeeper
score = scorekeeper()

def test_getPlayerScore():
    # Get the player's score
    assert score.get_player_score() == 100

# Win condition (Multiply winnings by 2)
def test_winCondition():
    print("Win Condition")
    assert score.set_bet(10) == True
    assert score.get_bet() == 10
    assert score.win() == True
    assert score.get_player_score() == 110

# Lose condition (Subtract what was bidded)
def test_loseCondition():
    # Used to make this test flexable (Can be tested individually or as a whole)
    balance = score.get_player_score()

    assert score.set_bet(10) == True
    assert score.get_bet() == 10
    assert score.lose() == True
    assert score.get_player_score() == (balance - 10)

def test_refund():
    # Test refunding
    assert score.set_bet(100) == True
    assert score.refund() == True

# ERROR TESTING
# Make a bid larger than the player's score
def test_largeBidError():
    assert score.set_bet(2000) == False

print("Please use \'pytest\' in the terminal OR VSCode\'s Testing tab to run the scoreboard tests!")