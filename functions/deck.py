from random import choice

class deck():
    def __init__(self):
        self.deck = []

    # Makes the deck
    def make_deck(self):
        numbers = ['A','K','Q','J',2,3,4,5,6,7,8,9,10]
        symbols = ['Clubs','Hearts','Spades','Diamonds']
        for number in numbers:
            for symbol in symbols:
                self.deck.append([number,symbol])


    # Since draw makes a random choice
    def shuffle_deck(self):
        self.make_deck()


    # Picks a card, and then removes it from the deck.
    def draw(self):
        card = choice(self.deck)    # Pick a card from the play deck
        self.deck.remove(card)      # Remove the card from the play deck
        return card                 # Return the card to who called it
    

    # These functions below are for troubleshooting purposes!
    # Shows the avaliable cards in the play deck
    def show_play_deck(self):
        for card in self.deck:
            print(card)
