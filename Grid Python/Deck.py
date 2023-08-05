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
                card = Card(suit, rank)
                card.load_image()  # Load the image for each card
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            raise ValueError("Deck is empty")
        return self.cards.pop()

    def get_remaining_cards(self):
        return len(self.cards)

    def draw_card_image(self, surface, x, y):
        if len(self.cards) > 0:
            card = self.cards[-1]
            card.draw(surface, x, y)