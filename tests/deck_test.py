# deck_test.py: Used to test deck functionality
import sys
import os
import pytest
# Used GitHub Co-Pilot to help me out with getting the functions path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))
import deck
card_deck = deck.deck()

# Make and show the play deck
def test_playDeck():
    assert card_deck.make_deck() == True
    assert card_deck.show_play_deck() == True

# Test a drawn card
def test_cardDrawn():
    card_deck.make_deck()           # Makes the deck (So this test can be ran individually)
    drawn_card = card_deck.draw()   # Draw a card
    print(str(drawn_card[0]) + " of " + drawn_card[1])
    assert drawn_card != False      # False means that there isn't a card that was drawn

print("Please use \'pytest\' in the terminal OR VSCode\'s Testing tab to run the scoreboard tests!")