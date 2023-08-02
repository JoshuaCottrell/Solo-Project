import random
from Card import Card
from Suit import Suit
from Rank import Rank

class Deck:
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def initialize_deck(self):
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            raise ValueError("Deck is empty")
        return self.cards.pop()

    def get_remaining_cards(self):
        return len(self.cards)
    
    def printCards(self):
        for card in self.cards:
            print(card)